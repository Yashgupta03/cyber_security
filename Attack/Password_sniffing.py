import paramiko
import tenetlib

def sshlogin(host,port,username,password) :
  try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_session = ssh.get_transport().open_session()
    if ssh_session.active :
      print("SSH login successful on %s: %s with username %s and pass %s" %(host,port,username,password))
  except Exception as e:
    return
  ssh.close()

def telnetlogin(host,port,username,password) :
  user = bytes(username + "\n","utf-8")
  passwd = bytes(password+ "\n","utf-8")

  tn=telnetlib.Telnet(host,port)
  tn.read_until(bytes("login: ","utf-8"))
  tn.write(user)
  tn.read_until(bytes("Password: ","utf-8"))
  tn.write(passwd)
  try:
    result = tn.expect([bytes("last login","utf-8")],timeout=2)
    if (result[0] >=0):
      print("Telnet successful login on %s: %s with username %s and password %s" %s(host,port,username,password))
    tn.close()
  except EOFERROR:
    print("failed as %s %s" %(username,password))


host = "127.0.0.1"
with open("defaults.txt","r") as f:
  for line in f:
    vals = line.split()
    username=vals[0].strip()
    password=vals[1].strip()
    sshlogin(host,22,username,password)
    telnetlogin(host,23,username,password)