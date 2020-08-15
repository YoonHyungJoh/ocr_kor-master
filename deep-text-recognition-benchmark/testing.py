import torch
import torch.nn as nn

old_model = torch.load("best_accuracy.pth", map_location=torch.device('cpu'))
for o in old_model.keys():
    print(o)
old_model.eval()
# model = TheModelClass(*args, **kwargs)
# model.load_state_dict(old_model['state_dict'])
# optimizer.load_state_dict(old_model['optimizer'])

# model = torch.load("best_accuracy.pth")

# class TheModelClass(nn.Module):
#     def __init__(self):
#         super(TheModelClass, self).__init__()
#         self.conv1 = nn.Conv2d(3, 6, 5)
#         self.pool = nn.MaxPool2d(2, 2)
#         self.conv2 = nn.Conv2d(6, 16, 5)
#         self.fc1 = nn.Linear(16 * 5 * 5, 120)
#         self.fc2 = nn.Linear(120, 84)
#         self.fc3 = nn.Linear(84, 10)
#
#     def forward(self, x):
#         x = self.pool(F.relu(self.conv1(x)))
#         x = self.pool(F.relu(self.conv2(x)))
#         x = x.view(-1, 16 * 5 * 5)
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = self.fc3(x)
#         return x
#
# model = TheModelClass()
# checkpoint = torch.load("best_accuracy.pth", map_location=torch.device('cpu'))
# model.load_state_dict(checkpoint['State_dict'])
# epoch = checkpoint['epoch']
# loss = checkpoint['loss']
# model.eval()