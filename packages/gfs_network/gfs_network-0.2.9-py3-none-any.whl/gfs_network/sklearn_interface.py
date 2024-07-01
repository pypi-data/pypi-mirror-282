from .select_gumbel_features import select_gumbel_features
import torch


class GFSNetwork:
    def __init__(
        self,
        batch_size=1,
        temperature_decay: float = 0.997,
        epochs: int = 200,
        balance: float = 1.0,
        device: str = "cpu",
        verbose: bool = False
    ) -> None:
        """Perform feature selection using GFSNetwork.

        Args:
            batch_size (int, optional): Batch size. Larger batch size speeds up training, but makes feature selection less aggresive. Defaults to 1.        
            temperature_decay (float, optional): Temperature decay. Defaults to 0.997.
            epochs (int, optional): Number of epochs. Defaults to 200.
            balance (float, optional): Balance between classification and feature selection. Larger value puts more weight on feature selection. Defaults to 1.0.
            device (str, optional): Device to use. Defaults to "cpu".
            verbose (bool, optional): Verbosity. Defaults to False.
        """
        self.scores_ = None
        self.device = device
        self.verbose = verbose
        self.temperature_decay = temperature_decay
        self.epochs = epochs
        self.network = None
        self.batch_size = batch_size
        self.balance = balance

    def fit(self, X, y, scale=True):
        # cast to torch
        if type(X) != torch.Tensor:
            X = torch.tensor(X)
            y = torch.tensor(y)

        # assert that y is one-hot encoded
        if len(y.shape) == 1:
            y = torch.nn.functional.one_hot(y.to(int))

        if scale:
            # perform whitening
            X = (X - X.mean(0)) / (X.std(0) + 1e-6)

        self.scores_, self.network = select_gumbel_features(
            X,
            y,
            self.device,
            self.verbose,
            temperature_decay=self.temperature_decay,
            epochs=self.epochs,
            batch_size=self.batch_size,
            fs_balance=self.balance
        )
        self.ranking_ = self.scores_.argsort()[::-1]
        return self

    @property
    def support_(self):
        assert self.scores_ is not None, "You must call fit before accessing support_"
        return self.scores_ > 0

    def transform(self, X):
        assert self.support_ is not None, "You must call fit before transform"
        return X[:, self.support_]

    def fit_transform(self, X, y):
        self.fit(X, y)
        return self.transform(X)
