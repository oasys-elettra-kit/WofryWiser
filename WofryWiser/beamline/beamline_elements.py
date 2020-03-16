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