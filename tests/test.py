# import pexpect
# 
# # a = pexpect.spawn('addr2line', ['-f', '-e', 'source.out'])
# a = pexpect.spawn('ls')
# 
# # a.expect('>')
# 
# print(a.read())
# a.sendline('1189')
# print(a.read())
# # a.sendeof()
# a.sendline('1181')

# a.expect('> ')
# print(a.after)

# import subprocess
# res = subprocess.Popen(['addr2line', '-f', '-e', 'source.out'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# 
# res.stdin.write(b'1189\n')
# print(res.stdout.read())
