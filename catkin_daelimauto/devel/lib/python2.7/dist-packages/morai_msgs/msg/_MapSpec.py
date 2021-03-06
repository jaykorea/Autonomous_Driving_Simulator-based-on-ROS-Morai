# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from morai_msgs/MapSpec.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class MapSpec(genpy.Message):
  _md5sum = "ff26999f16fc5ab8e3788072433240e9"
  _type = "morai_msgs/MapSpec"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 plane_coordinate_system
int32 utm_num

geometry_msgs/Vector3 utm_offset

string ellipse
float64 central_latitude
float64 central_meridian
float64 scale_factor
float64 false_easting
float64 false_northing
================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['plane_coordinate_system','utm_num','utm_offset','ellipse','central_latitude','central_meridian','scale_factor','false_easting','false_northing']
  _slot_types = ['int32','int32','geometry_msgs/Vector3','string','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       plane_coordinate_system,utm_num,utm_offset,ellipse,central_latitude,central_meridian,scale_factor,false_easting,false_northing

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MapSpec, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.plane_coordinate_system is None:
        self.plane_coordinate_system = 0
      if self.utm_num is None:
        self.utm_num = 0
      if self.utm_offset is None:
        self.utm_offset = geometry_msgs.msg.Vector3()
      if self.ellipse is None:
        self.ellipse = ''
      if self.central_latitude is None:
        self.central_latitude = 0.
      if self.central_meridian is None:
        self.central_meridian = 0.
      if self.scale_factor is None:
        self.scale_factor = 0.
      if self.false_easting is None:
        self.false_easting = 0.
      if self.false_northing is None:
        self.false_northing = 0.
    else:
      self.plane_coordinate_system = 0
      self.utm_num = 0
      self.utm_offset = geometry_msgs.msg.Vector3()
      self.ellipse = ''
      self.central_latitude = 0.
      self.central_meridian = 0.
      self.scale_factor = 0.
      self.false_easting = 0.
      self.false_northing = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2i3d().pack(_x.plane_coordinate_system, _x.utm_num, _x.utm_offset.x, _x.utm_offset.y, _x.utm_offset.z))
      _x = self.ellipse
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_5d().pack(_x.central_latitude, _x.central_meridian, _x.scale_factor, _x.false_easting, _x.false_northing))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.utm_offset is None:
        self.utm_offset = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.plane_coordinate_system, _x.utm_num, _x.utm_offset.x, _x.utm_offset.y, _x.utm_offset.z,) = _get_struct_2i3d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ellipse = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.ellipse = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.central_latitude, _x.central_meridian, _x.scale_factor, _x.false_easting, _x.false_northing,) = _get_struct_5d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2i3d().pack(_x.plane_coordinate_system, _x.utm_num, _x.utm_offset.x, _x.utm_offset.y, _x.utm_offset.z))
      _x = self.ellipse
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_5d().pack(_x.central_latitude, _x.central_meridian, _x.scale_factor, _x.false_easting, _x.false_northing))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.utm_offset is None:
        self.utm_offset = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.plane_coordinate_system, _x.utm_num, _x.utm_offset.x, _x.utm_offset.y, _x.utm_offset.z,) = _get_struct_2i3d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ellipse = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.ellipse = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.central_latitude, _x.central_meridian, _x.scale_factor, _x.false_easting, _x.false_northing,) = _get_struct_5d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i3d = None
def _get_struct_2i3d():
    global _struct_2i3d
    if _struct_2i3d is None:
        _struct_2i3d = struct.Struct("<2i3d")
    return _struct_2i3d
_struct_5d = None
def _get_struct_5d():
    global _struct_5d
    if _struct_5d is None:
        _struct_5d = struct.Struct("<5d")
    return _struct_5d
