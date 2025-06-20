# A Well-Conditioned Implementation of The Zipper Algorithm for Conformal Mappings

We aim to implement The Zipper Algorithm, an elementary procedure to develop a conformal map between particular regions, in such a way to minimize error. The Zipper Algorithm repeatedly applies various transformations to the complex plane, which can result in loss of precision in points that are close together and greater distance between faraway points. This project will implement each step of the map into its elementary transformations as described in Marshall and Rohde’s paper Convergence of a Variant of The Zipper Algorithm for Conformal Mapping. A function is said to be poorly conditioned if a small perturbation in the inputs results in a large change in outputs. We aim to conduct the entire mapping within the unit disc in attempts to eliminate some of the poorly conditioned steps, and in doing so provide bounds on the error that may be introduced in such a mapping.

## to run
poetry shell \
pytest \
jupyter lab
