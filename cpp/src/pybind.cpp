// We include all Pybind11 bindings in one file here, but you can split them into multiple modules.

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "../include/operators.h"

namespace py = pybind11;

PYBIND11_MODULE(_cpp, m) {
	// m.def("isosplit5", &isosplit5, "ISO-SPLIT clustering",
 //    py::arg("X").noconvert(),
 //    py::arg("y").noconvert(),
 //    py::arg("isocut_threshold"),
 //    py::arg("min_cluster_size"),
 //    py::arg("K_init"),
 //    py::arg("refine_clusters"),
 //    py::arg("max_iterations_per_pass"),
 //    py::arg("seed")
 //  );
}
