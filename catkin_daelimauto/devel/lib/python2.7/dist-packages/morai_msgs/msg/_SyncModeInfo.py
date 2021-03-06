# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from morai_msgs/SyncModeInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SyncModeInfo(genpy.Message):
  _md5sum = "6d9bc8fdf24a57461d5bcf823494e818"
  _type = "morai_msgs/SyncModeInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string master_id
bool status
uint64 frame

bool can_send_tick
"""
  __slots__ = ['master_id','status','frame','can_send_tick']
  _slot_types = ['string','bool','uint64','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       master_id,status,frame,can_send_tick

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SyncModeInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.master_id is None:
        self.master_id = ''
      if self.status is None:
        self.status = False
      if self.frame is None:
        self.frame = 0
      if self.can_send_tick is None:
        self.can_send_tick = False
    else:
      self.master_id = ''
      self.status = False
      self.frame = 0
      self.can_send_tick = False

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
      _x = self.master_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BQB().pack(_x.status, _x.frame, _x.can_send_tick))
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
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.master_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.master_id = str[start:end]
      _x = self
      start = end
      end += 10
      (_x.status, _x.frame, _x.can_send_tick,) = _get_struct_BQB().unpack(str[start:end])
      self.status = bool(self.status)
      self.can_send_tick = bool(self.can_send_tick)
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
      _x = self.master_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BQB().pack(_x.status, _x.frame, _x.can_send_tick))
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
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.master_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.master_id = str[start:end]
      _x = self
      start = end
      end += 10
      (_x.status, _x.frame, _x.can_send_tick,) = _get_struct_BQB().unpack(str[start:end])
      self.status = bool(self.status)
      self.can_send_tick = bool(self.can_send_tick)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_BQB = None
def _get_struct_BQB():
    global _struct_BQB
    if _struct_BQB is None:
        _struct_BQB = struct.Struct("<BQB")
    return _struct_BQB
