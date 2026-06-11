import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np

class SeqDataset(Dataset):
    def __init__(self, X, y, seq_len: int):
        self.X = X
        self.y = y
        self.seq_len = seq_len

    def __len__(self):
        return len(self.X) - self.seq_len

    def __getitem__(self, idx):
        x_seq = self.X[idx:idx + self.seq_len]
        y_tgt = self.y[idx + self.seq_len]
        return x_seq, y_tgt

def train_lstm(model, train_loader, val_loader, epochs=20, lr=1e-3, device="cpu"):
    model.to(device)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = torch.nn.MSELoss()

    for epoch in range(epochs):
        model.train()
        for xb, yb in train_loader:
            xb = xb.to(device).float()
            yb = yb.to(device).float()
            opt.zero_grad()
            preds = model(xb)
            loss = loss_fn(preds, yb)
            loss.backward()
            opt.step()

        # validation pass omitted for brevity
