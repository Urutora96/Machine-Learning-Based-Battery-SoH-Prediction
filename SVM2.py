import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, train_test_split
import time


def plot_decision_boundary(model, axis):
    x0, x1 = np.meshgrid(
        np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 5000)).reshape(-1, 1),
        np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 5000)).reshape(-1, 1),
    )
    x_new = np.c_[x0.ravel(), x1.ravel()]

    y_predict = model.predict(x_new)
    zz = y_predict.reshape(x0.shape)

    from matplotlib.colors import ListedColormap
    custom_cmap = ListedColormap(['#90CAF9', '#FFF59D', '#EF9A9A'])

    plt.contourf(x0, x1, zz, linewidth=5, cmap=custom_cmap)


def savemap(model, axis):
    x0, x1, x2 = np.meshgrid(
        np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 5000)).reshape(-1, 1),
        np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 5000)).reshape(-1, 1),
        np.linspace(axis[4], axis[5], int((axis[5] - axis[4]) * 5000)).reshape(-1, 1)
    )
    print(x0.shape)
    print(x1.shape)
    print(x2.shape)
    x_new = np.c_[x0.ravel(), x1.ravel(), x2.ravel()]
    y_predict = model.predict(x_new)
    np.savetxt('map.txt', y_predict, fmt="%d", delimiter=" ")


if __name__ == '__main__':
    data = np.genfromtxt('training data.txt', delimiter=',')
    x = data[:, [1, 2]]
    y = data[:, 0].astype(int)
    # scaler = StandardScaler()
    # x_std = scaler.fit_transform(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)

    start = time.time()
    svc = SVC(kernel='linear', class_weight='balanced', )
    c_range = np.logspace(-5, 15, 11, base=2)
    gamma_range = np.logspace(-9, 3, 13, base=2)
    degree_range = np.linspace(1, 10)
    param_grid = [{'kernel': ['linear'], 'C': c_range}]
    grid = GridSearchCV(svc, param_grid, cv=3, n_jobs=-1)
    clf = grid.fit(x_train, y_train)
    end = time.time()
    print('Running time: %s seconds' % (end - start))
    print(grid.predict(x_test))
    score = grid.score(x_test, y_test)
    print(score)
    # savemap(grid, [0.065, 0.090, 0.009, 0.013, 0.05, 0.1])
    plot_decision_boundary(clf, axis=[0.065, 0.09, 0.009, 0.013])
    plt.scatter(x[y==1, 0], x[y==1, 1], color="red", label='1st')
    plt.scatter(x[y==30, 0], x[y==30, 1], color="blue", label='30th')
    plt.scatter(x[y==50, 0], x[y==50, 1], color="yellow", label='50th')
    plt.xlabel('R0 (Rb)')
    plt.ylabel('R1 (Rsei)')
    plt.legend()
    plt.show()