import network
import espnow



def just_split(string0: str, separator: str):
  return str(string0).split(':')
    
def raw_text_addr_to_bytes(addr_in):
  """'ff:ff:ff:ff:ff:ff' to bytes([255,255,255,255,255,255])

  Args:
      addr_in (bytes): ____
  """
  _addr = just_split(addr_in, ":")
  for index, val in enumerate(_addr):
    _addr[index] = int(str(val), 16)
  return bytes(_addr)
    


class ESPN ():
  def __init__(self) -> None:
    
    #network driver setup
    self._net_wlan = network.WLAN(network.STA_IF)  # Or network.AP_IF | I don't know?
    # self._net_wlan.__init__() #just in case
    self._net_wlan.active(True)
    self._net_wlan.disconnect()

    #ESPNow set up
    self._EspNow = espnow.ESPNow()
    self._EspNow.__init__() #just in case
    self._EspNow.active(True)

    #default value
    self.sender_address :bytes = b'\x00' * 6
    self.recv_msg :bytes= "default_msg".encode("utf-8")
    self.addPeer('ff:ff:ff:ff:ff:ff') 
    
  
  def _DEBUG_peer_count(self) -> None:
    peer_count_and_encrypt = self._EspNow.peer_count()
    print(f'total peer {peer_count_and_encrypt[0]}\nencrypt peer: {peer_count_and_encrypt[1]}')

  def _get_peer_count(self) -> int:
    peer_count_and_encrypt = self._EspNow.peer_count()
    return peer_count_and_encrypt[0]


  def addPeer(self, addr_in :str,lmk_key :bytes= b'', channel :int= 0,) -> None:
    """Add/register the provided mac address as a peer. Additional parameters may also be specified as positional or keyword arguments (any parameter set to "None" will be set to it's default value

    Args:
        ADDR (str): The MAC address of the peer (such as "FF:FF:FF:FF:FF:FF")
        LMK_key (bytes, optional): The Local Master Key (LMK) key used to encrypt data transfers with this peer. a byte-string or bytearray or string of length espnow.KEY_LEN (16 bytes), or any non True python value, signifying an empty key which will disable encryption.  Defaults to b'0'.
        Channel (int, optional): The wifi channel (2.4GHz) to communicate with this peer. Must be an integer from 0 to 14. If channel is set to 0 the current channel of the wifi device will be used. Defaults to 0.

    Raises:
        OSError: if too many peer is register
    """
    # if self._get_peer_count() == self._EspNow.MAX_TOTAL_PEER_NUM:
    #   print(f'too many peer register\n{self._get_peer_count()} peer is already register')
    #   raise OSError
    # else:
    #   pass
   
    
    
    try:
      self._EspNow.add_peer(raw_text_addr_to_bytes(addr_in), lmk_key, channel)
    except OSError as err:
      # raise err
      pass

  def send(self, msg :str, MAC_of_recv="FF:FF:FF:FF:FF:FF") ->None:
    """Send the data contained in "msg" to the peer with given network mac address. !!!The peer MUST be registered with ESPNow.add_peer() before the message can be sent.

    Args:
        msg (str): string or byte-string up to espnow.MAX_DATA_LEN (250) bytes long.
        MAC_of_recv (str, optional): The MAC address of the receiver (such as "FF:FF:FF:FF:FF:FF"). Defaults to "FF:FF:FF:FF:FF:FF".
    """
    try:
      # self._EspNow.send(msg.encode("utf-8"), mac=raw_text_addr_to_bytes(MAC_of_recv))
      self._EspNow.send(raw_text_addr_to_bytes(MAC_of_recv), bytearray(msg,'utf-8'))
    except OSError as err:
      print("Sending error !\nSomething goes wrong when sending msg")
      raise err
  
  
  def isReadyToRead(self) -> bool:
    """Check if data is available to be read with readAsText/readAsNumber method.

    Returns:
        bool:
    """
    self.sender_address, self.recv_msg = self._EspNow.irecv(10)
    try:
      if self._EspNow.any():
        return True
      else:
        return False
    except:
      if self.recv_msg:
        return True
      else:
        return False
  
  def getSenderMAC(self) -> str:
    """Return the MAC address of the latest message.

    Returns:
        str: in the plain hex string. (such as "FF:FF:FF:FF:FF:FF")
    """
    sender_address_text :str = ""    
    sender_address_text :str = ":".join(format(i, "02X")  for i in self.sender_address)
    return sender_address_text

  def readAsText(self) -> str:
    return self.recv_msg.decode("utf-8") if self.recv_msg else ""
  
  def readAsNumber(self) -> float:
    if not self.recv_msg:
      return 0
    else:
      try:
        return float(self.recv_msg)
      except ValueError:
        pass
        return 0
