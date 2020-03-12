from syned.beamline.optical_element import OpticalElement as SynedOpticalElement
from syned.beamline.beamline_element import BeamlineElement

from LibWiser.Foundation import OpticalElement, PositioningDirectives


class WiserOpticalElement(SynedOpticalElement):
    def __init__(self,
                 name="Undefined", boundary_shape=None, # Syned object
                 native_CoreOptics=None, # A LibWiser.Optics.Optics object
                 native_PositioningDirectives=PositioningDirectives(), # LibWiser Foundation PositioningDirectives
                 isSource=False,
                 native_OpticalElement=None
                 ):

        # Init SynedOpticalElement
        # Fills: name, boundary_shape, as required by Syned
        super(WiserOpticalElement, self).__init__(name=name, boundary_shape=boundary_shape)

        if native_CoreOptics is not None:
            # Build the native Wiser OpticalElement
            # fills native_optical_element
            self.native_optical_element = OpticalElement(CoreOpticsElement=native_CoreOptics,
                                                         PositioningDirectives=native_PositioningDirectives,
                                                         Name=name,
                                                         # syned name and Wiser name will never be automatically synced...
                                                         IsSource=isSource)  # In case of source, to be discussed
        elif native_OpticalElement is not None:
            # In case the whole optical element is passed as an argument
            self.native_optical_element = native_OpticalElement
        else:
            print('Native OpticalElement not specified!')


class WiserBeamlineElement(BeamlineElement):
    def __init__(self, optical_element=WiserOpticalElement()):
        super(WiserBeamlineElement, self).__init__(optical_element=optical_element, coordinates=None)

    def get_coordinates(self):
        raise NotImplementedError("this method cannot be used in WISE 2")


#class WiserSource(W)

'''
# From beamline.optical_elements.wise_spheric_mirror.py

from syned.beamline.shape import Sphere
from wofrywise2.beamline.wise_optical_element import WiseOpticalElement
from wiselib2.Fundation import OpticalElement, PositioningDirectives
from wiselib2.Optics import MirrorSpheric

class WiseSphericMirror(WiseOpticalElement):
    def __init__(self, name="Undefined", spheric_mirror = MirrorSpheric(), position_directives=PositioningDirectives()):
        #:TODO boundary shape must be checked, is actually useless right now
        super(WiseSphericMirror, self).__init__(name=name,
                                                boundary_shape=Sphere(radius=spheric_mirror.f2),
                                                wise_optical_element = OpticalElement(Element=spheric_mirror,
                                                                                      PositioningDirectives=position_directives,
                                                                                      Name=name,
                                                                                      IsSource=False))
# From beamline.optical_elements.wise_plane_mirror.py

import numpy
from syned.beamline.shape import Plane
from wofrywise2.beamline.wise_optical_element import WiseOpticalElement
from wiselib2.Fundation import OpticalElement, PositioningDirectives
from wiselib2.Optics import MirrorPlane

class WisePlaneMirror(WiseOpticalElement):
    def __init__(self,
                 name="Undefined",
                 plane_mirror = MirrorPlane(L=0.4, AngleGrazing = numpy.deg2rad(2.5)),
                 position_directives=PositioningDirectives()):
        super(WisePlaneMirror, self).__init__(name=name,
                                              boundary_shape=Plane(),
                                              wise_optical_element = OpticalElement(Element=plane_mirror,
                                                                                    PositioningDirectives=position_directives,
                                                                                    Name=name,
                                                                                    IsSource=False))

# From beamline.optical_elements.wise_elliptic_mirror.py

import numpy
from syned.beamline.shape import Ellipse
from wofrywise2.beamline.wise_optical_element import WiseOpticalElement
from wiselib2.Fundation import OpticalElement, PositioningDirectives
from wiselib2.Optics import MirrorElliptic

class WiseEllipticMirror(WiseOpticalElement):
    def __init__(self,
                 name="Undefined",
                 elliptic_mirror = MirrorElliptic(f1 = 98, f2 = 1.2, Alpha = numpy.deg2rad(2.5), L = 0.4),
                 position_directives=PositioningDirectives()):
        #:TODO boundary shape must be checked, is actually useless right now

        max_0 = 0.0 if position_directives.XYCentre is None else position_directives.XYCentre[0]
        min_0 = 0.0 if position_directives.XYCentre is None else position_directives.XYCentre[1]

        super(WiseEllipticMirror, self).__init__(name=name,
                                                 boundary_shape=Ellipse(a_axis_min=-0.5*elliptic_mirror.f1 + min_0,
                                                                        a_axis_max=0.5*elliptic_mirror.f1 + min_0,
                                                                        b_axis_min=-0.5*elliptic_mirror.f2 + max_0,
                                                                        b_axis_max=-0.5*elliptic_mirror.f2 + max_0),
                                                 wise_optical_element = OpticalElement(Element=elliptic_mirror,
                                                                                       PositioningDirectives=position_directives,
                                                                                       Name=name,
                                                                                       IsSource=False))

# From beamline.optical_elements.wise_detector.py

import numpy
from wofrywise2.beamline.wise_optical_element import WiseOpticalElement
from wiselib2.Fundation import OpticalElement, PositioningDirectives
from wiselib2.Optics import Detector

class WiseDetector(WiseOpticalElement):
    def __init__(self,
                 name="Undefined",
                 detector = Detector(L=400e-6, AngleGrazing = numpy.deg2rad(90) ),
                 position_directives=PositioningDirectives()):
        super(WiseDetector, self).__init__(name=name,
                                           boundary_shape=None,
                                           wise_optical_element = OpticalElement(Element=detector,
                                                                                 PositioningDirectives=position_directives,
                                                                                 Name=name,
                                                                                 IsSource=False))
# From beamline.light_sources.wise_gaussian_source.py

from wofrywise2.beamline.wise_optical_element import WiseOpticalElement
from wiselib2.Fundation import OpticalElement, PositioningDirectives
from wiselib2.Optics import SourceGaussian


class WiseGaussianSource(WiseOpticalElement):
    def __init__(self, name="Undefined", source_gaussian = SourceGaussian(Waist0=0.0, Lambda=10.0), position_directives=PositioningDirectives()):
        #:TODO boundary shape must be checked, is actually useless right now
        super(WiseGaussianSource, self).__init__(name=name,
                                                 boundary_shape=None,
                                                 wise_optical_element = OpticalElement(Element=source_gaussian,
                                                                                       PositioningDirectives=position_directives,
                                                                                       Name=name,
                                                                                       IsSource=True))
'''