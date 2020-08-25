map = load('C:\Users\luowe\Desktop\IRP_code\map.txt');
map = map(:)';
[X, Y, Z] = meshgrid(linspace(0.009, 0.013, 20), linspace(0.05, 0.1, 250), linspace(0.065, 0.09, 124));
scatter3(X(:),Y(:),Z(:),5, map, 'filled');