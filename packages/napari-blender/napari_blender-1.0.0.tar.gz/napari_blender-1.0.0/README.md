# napari-blender

napari-blender is a plugin for napari that allows you to render 3D scenes using Blender.

This is a system that combines optical validation of model predictions by having different 3D visualizations and quantitative evaluation. Utilizing Blender’s rendering capabilities for deepening the understanding of nuclei segmentation for users with different levels of expertise. Examples are time-lapse animations (aimed to be generated from label data), opaque ground truth visualizations with solid prediction objects to compare prediction quality optically and 3D images where nuclei are coloured according to their prediction quality. To facilitate meaningful quantitative evaluation, different metrics are calculated for these predictions and displayed within the animation, such as the Jaccard index, Intersection over Union and the F1-score. The emphasis in this system is on operating it with limited technical knowledge, allowing for bridging between researchers and developers; but includes metrics that allow for a deeper understanding of performance for expert users.

Documentation can be found at https://living-technologies.github.io/napari-blender/
----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-blender` via [pip]:

    pip install napari-blender



To install latest development version :

    pip install git+https://github.com/Living-Technologies/napari-blender.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [Mozilla Public License 2.0] license,
"napari-blender" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/Living-Technologies/napari-blender/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
