// We include all Pybind11 bindings in one file here, but you can split them into multiple modules.

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <math.h>

namespace py = pybind11;

template <typename T>
void km_laplace(
  py::array_t<T> X,
  py::array_t<T> Y,
  float K
  )
// Kuramoto Laplacian 
{
  auto X_data = X.template unchecked<2>(); 
  auto Y_data = Y.template mutable_unchecked<2>(); 
  const int m = X.shape(0);
  const int n = X.shape(1);

  int i = 0, j = 0;
  for (i = 0; i < m; i++) {
    for (j = 0; j < n; j++) {
      auto x = X_data(i, j);

      if (i > 0) Y_data(i, j) += K * sin(X_data(i-1, j) - x);
      if (j > 0) Y_data(i, j) += K * sin(X_data(i, j-1) - x);
      if (i < m-1) Y_data(i, j) += K * sin(X_data(i+1, j) - x);
      if (j < n-1) Y_data(i, j) += K * sin(X_data(i, j+1) - x);
    }
  }
}

PYBIND11_MODULE(_cpp, m) {
	m.def("km_laplace", &km_laplace<double>, "Kuramoto Laplace operator",
    py::arg("X").noconvert(),
    py::arg("Y").noconvert(),
    py::arg("K")
  );
  m.def("km_laplace", &km_laplace<float>, "Kuramoto Laplace operator",
    py::arg("X").noconvert(),
    py::arg("Y").noconvert(),
    py::arg("K")
  );
}
