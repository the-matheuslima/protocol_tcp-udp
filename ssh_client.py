import paramiko

host = ''
user = 'kali'
passwd = 'kali'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:
    sdin, stdout, sstderr = client.exec_command(input('Comando: '))
    for line in stdout.readlines():
        print(line.strip())



print(stdout.readlines())