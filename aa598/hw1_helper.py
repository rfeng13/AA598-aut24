import jax.numpy as jnp
import jax
import numpy as np
import matplotlib.pyplot as plt

from torch.utils.data import Dataset
import torch
import pickle
from torch.utils.data import DataLoader

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets



class TrajectoryData(Dataset):
    def __init__(self, filename):
        with open('%s.pickle'%filename, 'rb') as handle:
            wave_data = pickle.load(handle)
        self.history = torch.tensor(wave_data["history"])
        self.future = torch.tensor(wave_data["future"])

    def __len__(self):
        return len(self.history)

    def __getitem__(self, idx):
        return self.history[idx], self.future[idx]



def train(model, optimizer, dataloader, criterion, num_epochs):
    # Training loop
    for epoch in range(num_epochs):
        model.train()  # Set model to training mode
        running_loss = 0.0

        for batch_idx, (data, target) in enumerate(dataloader):
            optimizer.zero_grad()        # Zero the gradients
            output = model(data)         # Forward pass
            loss = criterion(output, target)  # Compute loss
            loss.backward()              # Backpropagation
            optimizer.step()             # Update weights

            running_loss += loss.item()
            if batch_idx % 20 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Step [{batch_idx}/{len(dataloader)}], Loss: {loss.item():.4f}')

        print(f'Epoch {epoch+1} completed with average loss: {running_loss/len(dataloader):.4f}')

    print("Training finished!")

    return model, optimizer


def plot_data_regression(history, future, prediction, index, xlims=[-11, 5], ylims=[-2,2]):
    # history, future = data_list[index]
    history_length = history.shape[-1]
    future_length = future.shape[-1]
    prediction_length = prediction.shape[-1]
    ts_history = np.arange(-history_length,0)
    ts_future = np.arange(future_length)
    ts_prediction = np.arange(prediction_length)

    plt.figure(figsize=(8, 4))
    plt.plot(ts_history, history[index].cpu().numpy(), marker='o', linestyle='--', label="History")
    plt.plot([-1,0], [history[index][-1].cpu().numpy(), future[index][0].cpu().numpy()], marker='o', linestyle='--', color="C0")

    plt.plot(ts_future, future[index].cpu().numpy(), markersize=7, marker='o', linestyle='--', label="Ground truth")
    plt.plot(ts_prediction, prediction[index].detach().numpy(), markersize=4, marker='o', linestyle='--', label="Prediction")

    plt.xlabel('Steps')
    plt.ylabel('Value')
    plt.legend()
    plt.xlim(xlims)
    plt.ylim(ylims)
    plt.grid(True)
    plt.show()

def plot_data_generative(history, future, prediction, index, xlims=[-11, 5], ylims=[-2,2]):
    history_length = history.shape[-1]
    future_length = future.shape[-1]
    prediction_length = prediction.shape[-1]
    ts_history = np.arange(-history_length,0)
    ts_future = np.arange(future_length)
    ts_prediction = np.arange(prediction_length)

    plt.figure(figsize=(8, 4))
    plt.plot(ts_history, history[index].cpu().numpy(), marker='o', linestyle='--', label="History")
    plt.plot(ts_future, future[index].cpu().numpy(), markersize=7, marker='o', linestyle='--', label="Ground truth")
    for i in range(prediction.shape[1]):
        plt.plot(ts_prediction, prediction[:,i,index,:].detach().numpy().T, markersize=2, marker='o', linestyle='-', color="C2", alpha=0.2)
    plt.plot([-1,0], [history[index][-1].cpu().numpy(), future[index][0].cpu().numpy()], marker='o', linestyle='--', color="C0")

    plt.xlabel('Steps')
    plt.ylabel('Value')
    plt.legend(['History', "Ground Truth", "Prediction"])
    plt.xlim(xlims)
    plt.ylim(ylims)
    plt.grid(True)
    plt.show()