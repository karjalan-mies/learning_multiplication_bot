from random import randint

for_correct = [
    'CAACAgIAAxkBAAIcGWLB_jLFNdeOyWL_mAqGsZd39rHBAAKgAAOhjEEL20QHqtX7uHcpBA',
    'CAACAgIAAxkBAAIcHWLB_sud7lIpaN31p-8L78R5vuFgAAKuAAOhjEELD_YdkLkfie8pBA',
    'CAACAgIAAxkBAAIcJWLB_zJPWdkTSq-UprJJlgLSRrJtAAK3AAOhjEELxYbQsgtHLcUpBA',
    'CAACAgIAAxkBAAIcJ2LB_1MDO2Gi9dBTvlg89rVHivsfAAK7AAOhjEELs5eZCFmPDK8pBA',
    'CAACAgIAAxkBAAIcK2LB_8I67dh3em65jUO0a2ECufqeAAKeAAOhjEELC_TvrY4YL_gpBA'
]

for_wrong = [
    'CAACAgIAAxkBAAIcG2LB_m2Pzt_IPnbdIwxWisLHwkLtAAKsAAOhjEELfa5tc6jLV7UpBA',
    'CAACAgIAAxkBAAIcH2LB_uY4u9YbQSgKI94prxv9K7WTAAKxAAOhjEELDlQy4FHqxgUpBA',
    'CAACAgIAAxkBAAIcIWLB_wI9BiFU990RRTIEMwI26t59AAKyAAOhjEELWTLPxc3ThMEpBA',
    'CAACAgIAAxkBAAIcI2LB_yH7Qwszt_aLvhfGqFEAAdkoKwACtgADoYxBC5r_93ZTJTaYKQQ',
    'CAACAgIAAxkBAAIcKWLB_4pzbxds-1nREWIiqmo30zUNAAKjAAOhjEELEUUUnzcjamEpBA'
]


def get_sticker(correct_answer: bool) -> str:
    if correct_answer:
        return for_correct[randint(0, len(for_correct)-1)]
    else:
        return for_wrong[randint(0, len(for_wrong)-1)]
