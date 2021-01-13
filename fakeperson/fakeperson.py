import os
import datetime
import random
import string

REAL_NAMES = dict()
ONLY_NAMES = []

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def realnames():
    names_csv = os.path.join(CUR_DIR, 'names.csv')
    with open(names_csv, 'r') as fp:
        for line in fp:
            name, gender = line.split(",")
            REAL_NAMES[name] = gender.strip("\n")

realnames()
def only_names():
    only_names_csv = os.path.join(CUR_DIR, 'only_names.csv')
    with open(only_names_csv, 'r') as fp:
        for line in fp:
            names = line.split(",")
            for name in names:
                name = name.strip("\n")
                if len(name) >= 2:
                    ONLY_NAMES.append(name)

only_names()

def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st

def first_name():  #   随机取姓氏字典
    first_name_list = [
        '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
        '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
        '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
        '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
        '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
        '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
        '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    n = random.randint(0, len(first_name_list) - 1)
    f_name = first_name_list[n]
    return f_name

def second_name():
    # 随机取数组中字符，取到空字符则没有second_name
    second_name_list = [GBK2312(), '']
    n = random.randint(0, 1)
    s_name = second_name_list[n]
    return s_name

def last_name():
    return GBK2312()

def create_name():
    name = first_name() + second_name() + last_name()
    return name


def fake_name():
    _first_name = first_name()
    _second_name = second_name()
    _second_name = random.choice(ONLY_NAMES)[1]
    realname = random.choice(list(REAL_NAMES.keys()))
    _last_name = realname[-1]
    return _first_name + _second_name + _last_name

def fake_gender(name=None):
    if name is None:
        return random.choice(["男", "女"])

    last_name = name[-1]
    for name, gender in REAL_NAMES.items():
        if name.endswith(last_name):
            return gender

    return random.choice(["男", "女"])

def fake_birthdate():
    # 35 - 88吧 45以上的多些
    year = random.randrange(2019-88, 2019-35)
    month = random.randrange(1, 12)
    day = random.randrange(1, 31)
    try:
        return datetime.date(year, month, day)
    except ValueError:
        day = random.randrange(1, 28)
    return datetime.date(year, month, day)


def fake_phone():
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
    '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    start = random.choice(num_start)
    end = ''.join(random.sample(string.digits,8))
    res = start+end
    return res

def fake_person():
    name = fake_name()
    gender = fake_gender(name)
    birthdate = fake_birthdate()
    phone = fake_phone()
    return dict(name=name, gender=gender, birthdate=birthdate, phone=phone)
