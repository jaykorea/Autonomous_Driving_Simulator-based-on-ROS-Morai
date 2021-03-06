# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from morai_msgs/MoraiMapSpecSrvRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import morai_msgs.msg

class MoraiMapSpecSrvRequest(genpy.Message):
  _md5sum = "70ff63378fe8f24cafd7c26339994774"
  _type = "morai_msgs/MoraiMapSpecSrvRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """MapSpecIndex request

================================================================================
MSG: morai_msgs/MapSpecIndex
bool load_map_data"""
  __slots__ = ['request']
  _slot_types = ['morai_msgs/MapSpecIndex']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       request

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MoraiMapSpecSrvRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.request is None:
        self.request = morai_msgs.msg.MapSpecIndex()
    else:
      self.request = morai_msgs.msg.MapSpecIndex()

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
      _x = self.request.load_map_data
      buff.write(_get_struct_B().pack(_x))
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
      if self.request is None:
        self.request = morai_msgs.msg.MapSpecIndex()
      end = 0
      start = end
      end += 1
      (self.request.load_map_data,) = _get_struct_B().unpack(str[start:end])
      self.request.load_map_data = bool(self.request.load_map_data)
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
      _x = self.request.load_map_data
      buff.write(_get_struct_B().pack(_x))
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
      if self.request is None:
        self.request = morai_msgs.msg.MapSpecIndex()
      end = 0
      start = end
      end += 1
      (self.request.load_map_data,) = _get_struct_B().unpack(str[start:end])
      self.request.load_map_data = bool(self.request.load_map_data)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from morai_msgs/MoraiMapSpecSrvResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import morai_msgs.msg

class MoraiMapSpecSrvResponse(genpy.Message):
  _md5sum = "3ece60c7ec9cd22d0f3d7405c24531d1"
  _type = "morai_msgs/MoraiMapSpecSrvResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """MapSpec response

================================================================================
MSG: morai_msgs/MapSpec
int32 plane_coordinate_system
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
  __slots__ = ['response']
  _slot_types = ['morai_msgs/MapSpec']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       response

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MoraiMapSpecSrvResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.response is None:
        self.response = morai_msgs.msg.MapSpec()
    else:
      self.response = morai_msgs.msg.MapSpec()

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
      buff.write(_get_struct_2i3d().pack(_x.response.plane_coordinate_system, _x.response.utm_num, _x.response.utm_offset.x, _x.response.utm_offset.y, _x.response.utm_offset.z))
      _x = self.response.ellipse
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_5d().pack(_x.response.central_latitude, _x.response.central_meridian, _x.response.scale_factor, _x.response.false_easting, _x.response.false_northing))
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
      if self.response is None:
        self.response = morai_msgs.msg.MapSpec()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.response.plane_coordinate_system, _x.response.utm_num, _x.response.utm_offset.x, _x.response.utm_offset.y, _x.response.utm_offset.z,) = _get_struct_2i3d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.response.ellipse = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.response.ellipse = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.response.central_latitude, _x.response.central_meridian, _x.response.scale_factor, _x.response.false_easting, _x.response.false_northing,) = _get_struct_5d().unpack(str[start:end])
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
      buff.write(_get_struct_2i3d().pack(_x.response.plane_coordinate_system, _x.response.utm_num, _x.response.utm_offset.x, _x.response.utm_offset.y, _x.response.utm_offset.z))
      _x = self.response.ellipse
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_5d().pack(_x.response.central_latitude, _x.response.central_meridian, _x.response.scale_factor, _x.response.false_easting, _x.response.false_northing))
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
      if self.response is None:
        self.response = morai_msgs.msg.MapSpec()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.response.plane_coordinate_system, _x.response.utm_num, _x.response.utm_offset.x, _x.response.utm_offset.y, _x.response.utm_offset.z,) = _get_struct_2i3d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.response.ellipse = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.response.ellipse = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.response.central_latitude, _x.response.central_meridian, _x.response.scale_factor, _x.response.false_easting, _x.response.false_northing,) = _get_struct_5d().unpack(str[start:end])
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
class MoraiMapSpecSrv(object):
  _type          = 'morai_msgs/MoraiMapSpecSrv'
  _md5sum = '05d746a24a1f7725a363510d4264a323'
  _request_class  = MoraiMapSpecSrvRequest
  _response_class = MoraiMapSpecSrvResponse
