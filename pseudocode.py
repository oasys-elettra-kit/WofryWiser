# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:54:14 2020

@author: Mike - Manfredda
"""

from syned.beamline.optical_element import OpticalElement as SynedOpticaElement

from wiselib2.Fundation import OpticalElement


# Option1: Anonymous wrapper, from named Optics to anonymous Syned
class WiseOpticalElement(SynedOpticaElement):

    def __init__(self,
						name="Undefined",
						boundary_shape = None, #syned object
						native_CoreOptics = None, # a LibWISEr.Optics.Optics object
						native_PositioningDirectives = lw.Fundation.PositioningDirectives()
						):
						# we might also add the parameter
#						native_OpticalElement = none
						# then decide what to take. But it is confusing

		# Init SynedOpticalElement
		# Fills: name, boundary_shape
		super(WiseOpticalElement, self).__init__(name=name,
                                                 boundary_shape=boundary_shape)


		# Build the native Wiser OpticalElement
		# fills native_optica_element
		self.native_optical_element = OpticalElement(CoreOpticsElement=native_CoreOptics,
																	   PositioningDirectives=native_PositioningDirectives,
																	   Name = name, #syned name and Wiser name will never be automatically synced...
																		IsSource=False))

#
#%% If we want  to create a named WiseEllipticMirror based on Wise Optcail Element
		# What is strange in this function is that nowhere is stated that it is an ellipse...
		# only the default value
		#
class WiseEllipticMirror(WiseOpticalElement):

	def __init__(self, **kwargs): # we do not need

		# default value
		if native_CoreOptics == None:
			native_CoreOptics = MirrorElliptic(f1 = 98, f2 = 1.2, Alpha = numpy.deg2rad(2.5), L = 0.4)

		# if there were specific calculations on boundary shape (but I do not think
		# there will be.... I think this formulas are wrong. And I am pretty sure that
		# there is only one way to define the concept of 2D boundary shape starting from our
		# 1D objects...)
        max_0 = 0.0 if position_directives.XYCentre is None else position_directives.XYCentre[0]
        min_0 = 0.0 if position_directives.XYCentre is None else position_directives.XYCentre[1]

        self.boundary_shape=Ellipse(a_axis_min=-0.5*elliptic_mirror.f1 + min_0,
                                    a_axis_max=0.5*elliptic_mirror.f1 + min_0,
                                    b_axis_min=-0.5*elliptic_mirror.f2 + max_0,
									          b_axis_max=-0.5*elliptic_mirror.f2 + max_0)



#%%

# But also looking at this, what is "elliptic" is the "default" value....and the name...nothing more.

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


