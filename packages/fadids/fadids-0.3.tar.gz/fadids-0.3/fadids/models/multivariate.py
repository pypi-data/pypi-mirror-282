from streamad.model import RrcfDetector, HSTreeDetector
from fadids.models.container import MultivariateContainer, AbstractContainer
import numpy as np
from math import floor
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


class RrcfAD(MultivariateContainer):
    def __init__(self, threshold=10, initialization=300, num_trees=10, tree_size=10) -> None:
        self.model = RrcfDetector(num_trees=num_trees, tree_size=tree_size)
        super().__init__(self.model, threshold, initialization)
        self.threshold = threshold
        self.initialization = initialization


class HSTreeAD(AbstractContainer):
    def __init__(self, threshold=85000, low_threshold=500, tree_height=10, tree_num=10, initialization: int = 600) -> None:
        self.model = HSTreeDetector(tree_height=tree_height, tree_num=tree_num)
        super().__init__(self.model, threshold, initialization)
        self.low_threshold = low_threshold

    def fit(self, data: np.ndarray):
        for x in data:
            score = self.model.fit_score(x)
            try:
                if ((score > self.threshold) | (score < self.low_threshold)) & (len(self.anomalies_scores) > self.initialization):
                    self.predictions.append(True)
                else:
                    self.predictions.append(False)
            except TypeError:
                self.predictions.append(False)
            self.anomalies_scores.append(score)


class IforestASD():
    """
    An anomaly detection system based on the Isolation Forest algorithm. This system uses a sliding window
    approach to process incoming data streams and detect anomalies based on drift in data characteristics.

    Attributes:
        window_len (int): Length of the moving window for data processing.
        overlap (float): Fraction of overlap between consecutive windows.
        n_estimators (int): Number of trees in the Isolation Forest.
        contamination (float): The proportion of outliers expected in the data.
        threshold (float): Threshold for determining significant drift, indicating anomalies.
        random_state (int, optional): Seed for the random number generator.
        verbose (bool): Flag to enable verbose output during computation.
    """

    def __init__(self, window_len=50, overlap=0.25, n_estimators=50, contamination=0.5, threshold=0.5, random_state=None, verbose=False) -> None:
        self.window_len = window_len
        self.overlap = overlap
        self.n_estimators = n_estimators
        self.contamination = contamination
        self.threshold = threshold
        self.random_state = random_state
        self.iforest = None
        self.initialized = False
        self.last_anomaly_score = None
        self.drift_scores = {}
        self.last_sample = None
        self.n_values = 0
        self.verbose = verbose
        self._create()
        self.step = floor(self.window_len * self.overlap)

    def fit(self, incoming_sample):
        """
        Fits the model to incoming data samples. This method updates the state of the model with
        each incoming data sample and checks for anomalies.

        Args:
            incoming_sample (array-like): New data to be added to the model's window for analysis.
        """
        self.n_values += len(incoming_sample)
        if self.last_sample is not None:
            current_sample = np.vstack((self.last_sample, incoming_sample))
        else:  # last_sample still Nonetype
            current_sample = incoming_sample
        if len(current_sample) > self.window_len:
            for index in range(0, len(current_sample), self.step):
                if index >= self.window_len:
                    self._predict(
                        current_sample[index-self.window_len:index], idx=self.n_values + index)
        try:
            self.last_sample = current_sample[-self.window_len:]
        except KeyError:
            self.last_sample = current_sample

    def _predict(self, sample: np.ndarray, idx) -> None:
        """
        Internal method to make predictions on a window of data. This method also handles drift detection
        and anomaly reporting.

        Args:
            sample (np.ndarray): The data sample to analyze.
            idx (int): The index of the data sample in the stream.
        """
        scaler = StandardScaler()
        sample = scaler.fit_transform(sample)
        drift = 0
        # Calcul anomalies only if already fitted
        if self.initialized:
            score = self._get_anomaly_scores(sample)
            drift = np.abs(score - self.last_anomaly_score)
            if drift >= self.threshold:
                self._report_anomaly(idx)
                self._create()
            else:
                self.last_anomaly_score = score
        self._fit(sample)
        self.drift_scores[idx - self.window_len - 1] = drift

    def _create(self) -> IsolationForest:
        """
        Creates a new Isolation Forest model using the instance's parameters.
        """
        self.iforest = IsolationForest(
            n_estimators=self.n_estimators, contamination=self.contamination, random_state=self.random_state)

    def _fit(self, sample) -> None:
        """
        Fits the Isolation Forest model to the sample.

        Args:
            sample (np.ndarray): The data sample to fit the model.
        """
        self.iforest.fit(sample)
        self.last_anomaly_score = self._get_anomaly_scores(sample)
        self.initialized = True

    def _report_anomaly(self, idx):
        """
        Reports an anomaly detected at a specific index.

        Args:
            idx (int): Index at which the anomaly is detected.
        """
        message = f"Anomaly detected at index {idx}"
        print(message)

    def _get_anomaly_scores(self, sample):
        """
        Computes anomaly scores for the given sample.

        Args:
            sample (np.ndarray): The sample to compute the anomaly scores for.

        Returns:
            float: Anomaly rate in the sample.
        """
        predictions = self.iforest.predict(sample)
        total_anomalies = (predictions < 0).sum()
        anomaly_rate = total_anomalies / len(sample)
        return anomaly_rate

    def get_anomalies(self):
        """
        Retrieves a list of indices where anomalies have been detected based on the threshold.

        Returns:
            List[int]: Indices of detected anomalies.
        """
        return [key for key, value in self.drift_scores.items() if value > self.threshold]

    def get_scores(self):
        """
        Returns the dictionary of drift scores recorded during data processing.

        Returns:
            dict: Drift scores indexed by data indices.
        """
        return self.drift_scores
