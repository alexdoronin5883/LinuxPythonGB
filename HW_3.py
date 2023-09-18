# фикстура дописывает в  файл stat.txt

@pytest.fixture(autouse=True)
def stat():
    yield
    stat = getout("cat /proc/loadavg")
    checkout("echo 'time: {} count:{} size: {} load: {}'>> stat.txt".format(datetime.now().strftime("%H:%M:%S.%f"), data["count"], data["bs"], stat), "")

# команды 7z -t (тип архива). Вынести этот параметр в конфиг
 def test_step4(self, start_time):
       self.save_log(start_time, "log4.txt")
       assert ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z t"
           " arx2.{}".format(data["folder_out"], data["type"]), "Everything is Ok"), "test4 FAIL"


   def test_step5(self, start_time):
       self.save_log(start_time, "log5.txt")
       assert ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z u"
           " arx2.{}".format(data["folder_in"], data["type"]), "Everything is Ok"), "test5 FAIL"
"""
folder_in: /home/vboxuser/tst
folder_out: /home/vboxuser/out
folder_ext: /home/vboxuser/folder1
folder_ext2: /home/vboxuser/folder2
count: 5
bs: 1M
ip: **************
user: user
passwd: ***********
pkgname: p7zip-full
type: 7z
"""
