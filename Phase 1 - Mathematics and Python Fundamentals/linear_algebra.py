import numpy as np
import matplotlib.pyplot as plt

print("🚀 Piro AI - Phase 1: Linear Algebra Demo")
print("=" * 50)

# 1. VEKTÖR İŞLEMLERİ
print("1. VECTOR OPERATIONS")
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 • v2 (dot product) = {np.dot(v1, v2)}")
print(f"||v1|| (norm) = {np.linalg.norm(v1):.2f}")

# 2. MATRİS İŞLEMLERİ
print("\n2. MATRIX OPERATIONS")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"A = \n{A}")
print(f"B = \n{B}")
print(f"A × B = \n{np.dot(A, B)}")
print(f"det(A) = {np.linalg.det(A):.2f}")
print(f"A⁻¹ (inverse) = \n{np.linalg.inv(A)}")

# 3. EIGEN DEĞERLER
print("\n3. EIGENVALUES & EIGENVECTORS")
eigenvals, eigenvecs = np.linalg.eig(A)
print(f"Eigenvalues: {eigenvals}")
print(f"Eigenvectors: \n{eigenvecs}")

# 4. GÖRSELLEŞTİRME
print("\n4. VISUALIZATION")
x = np.linspace(-10, 10, 100)
y = x**2  # Quadratic function

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y, 'b-', linewidth=2)
plt.title('f(x) = x²')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.imshow(A, cmap='viridis', interpolation='nearest')
plt.title('Matrix A')
plt.colorbar()

plt.tight_layout()
plt.savefig('linear_algebra_demo.png', dpi=150, bbox_inches='tight')
print("📊 Grafik kaydedildi: linear_algebra_demo.png")

print("\n🎉 Lineer Cebir Temelleri Tamamlandı!")