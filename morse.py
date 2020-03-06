def count_call(fn):
    def _counter(*args, **kwargs):
        _counter.call += 1
        return fn(*args, **kwargs)
    _counter.call = 0
    return _counter


def word_to_morse(word):
    alpha_morse = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
    }
    morse = ""
    for c in word.lower():
        morse += alpha_morse[c]
    return morse


def phrase_start_with(phrase, word):
    if phrase[:len(word)] == word:
        return True
    return False


@count_call
def count(phrase, l_word, index):
    print("recu = {}".format(count.call))
    cpt = 0
    # print("---------------")
    # print("phrase: {}".format(phrase))
    # print("cpt: {}, index: {}".format(cpt, index))
    if len(phrase) == 0:
        # print("ret 1 !!")
        return 1
    if index >= len(l_word):
        # print("ret 0 ..")
        return 0
    # print("word: '{}'".format(l_word[index]))
    if phrase_start_with(phrase, l_word[index]):
        l_sub_word = [word for word in l_word if word in phrase]
        cpt += count(phrase[len(l_word[index]):], l_sub_word, 0)
        # cpt += count(phrase[len(l_word[index]):], l_word, 0)
    cpt += count(phrase, l_word, index + 1)
    return cpt


if __name__ == "__main__":
    # l = "......-...-..---.-----.-..-..-.."
    l = ".-...-.-...--......--....------.-.....---..--.-.----...-----.-.........-..--.-.-.----....--...-.--.--.--.--...-.-..--....--.--.-....--.-.-..--..-...-..-...-.......-.......-....--.--...-.-.......----....-.-.---..-.-.-.....-.-..----.--...-....--.-..-..-...-.........---...-.-.--..-.----....-..-.....--..-.-.-...........--.-.......--...-....---...-..---..-..--.--.....-.-.-..-.-.----.......-..-..-.----.--.-.-.---.-...-.....-....---..-..-..-----.-......-.-..---.-....--.-..-..--..-....-........-.-.....--...-....----.-......-...---.-...-.....-.-.-...----..-...........-.--.-.-.-....-..-..-.....-.-...-....-....-.-.-.-..--.---..-.-..-...--.-..--..-..-.--........-.-..-.-.----...---..-...-.-..-.-..--.-.-.-......-........--.-..-.-......---.-..-..-...--.-..-.-.........-...-..-...-.....--.-..-....--.----.-.-.-..-.--..----...--..-.-.------.....-..-.....----...--...--.-..-.-........--.-..-..--..-..-.-..-.--..--.-.-....-...-.-.----...-----.-.........--.-.----......-...-.-.-.-------..-....--..-.-.-...-.-.......-.-.-......-.-.-...-.-....--...-..-...-..-.-.-.....-..--.-..-..-...-.-.-...-..-.-.........---..--...-.--..--...-...-..-..--....----.-..--..-..-.--........-....--...-......-.......--.-.......--....-.--...---.-.......--..-...-....-....-...-.-..-.-.-------..--...-.-..--..----..--.--.--.-.--..-.......-....-...-...-......--..-.-.-...-.-...-.-..-------.-.-.-...-.-..-..-...-.-.--.-.-...-..--..-..--....----.-..--..-..-.--.......--.-..-..-.-..--....----.-...--.....----...--.-..-...--...-........--.-.-......----.-............-.---.....-.-.....-.-.-------.-.-.-..-..-.-..-....-...-..-...-.-.--.-.--.-...--..-.-...--.-...-...-..-.....-..-.-.-.---.-..-.-...------..-.-.-........-..-.--.-..-.-.-.-.......-.-..-.-..--..----..-.-.......-..-...-..-.-.-.....--..-.-..-....-..-.-...--......-...-...-.....----.-....-.........-.-..-....-...---------.-.-...-..---..-.-..--..--.-.-------..--...-.-..--..----....--.-.-...-..--.....-..-..--....----.-..--..-..-.--.........--..-.-.--..-...-..--.-.....-.-....--..-.-....--..---..--.-....--..-.-....--...--.---..-...-.--.-.-..-........-.-....--...-........--..-.-..-...-...-...--..----.-.-......-...-....-...--....--.-...-......---.-.....-.----.-----.-.-.-.....-...--...-.........--..-.-...--.....-..-.--.-.-..-..-....--..--.--...-...--.....-...------.-....--..-.-.--...-......--.-..-..-......-...-.-..--..........----..--....-..-...-.-.--..-.-..-...-...---....-.-....--...---.--..-...-.-..---..-.---..--..-...--.-.......-...-...-.-..--...--....-....--.-..-.-....--.-.----.--.----...---..-...---..--...-...-.-.---.....-...-......-.--.....--.......-....-.-..----........-....-.-.-......-.....-..-...--.-...-----.--..-...-.-.---..---.--.....-...-..-.-...-..--..----.-....-...-..........-..........------.-.---.-...-.-..-..-......-.-..........-.---.-.......-...-......--.-..-..-..--.-..-.....-..--.-...--.-..----.....--..-.....-...-.--..-....-.--..-.-.--.........-.--..----....--.-.-...-..--.....-.-.-.---.-...-..--.-.-.....-..--.--.--.-.-.--..-....-....-.-----.-.....--.-..-..-.....-.-...-.-....-.-..--....-.-...-.--..--...-...-...-.-.-..-..-...-...--.-.-.-.....-.-...-..-.--.-..-.-.-.-..-..--..........----..-..-.------..-.-.-........-..-.-...-.-.-..-.......-..-.--.-..-.-.-.-.....-......-..-......-..--.-..-..-...-.-..-.-.-..---....-...---.-.-...-..--.-.-.-.-......--.-...----.-.-.-.-.---.-....--...-..-...-..-.-.-.--..----.----........-...-......-.....----.-.--..-....-.....--...-...........--.-..-..--..-.-.--.-..-..-..--.-..-.....--..--.--....--.-.....-..-.-..--.-.--....--...-......-...-..-.....---....--..--..-......-.-..-....-.-....-....-.-.-..----.-....-...-.-...---.--...-.-..-........-......-....--..-..--..-.--....-...-.-.---..-.-...--.-.--.-.-------..--...--.-..-..-..-.-----.-......-....---..-....--..-.-.-..---.-....--.-..-..-...--.-..-.--..--.-...---.--.-..-...-..-..........--.-..-..--..-.-.....-..-..-..--...--.---..-.-.-......-.-....-.---..-...-...-.-.....-.-....-...---.-.-...-..--.-.-.-.-......--.-...-...--....-...-.------....-....--..-.--..--.--...-..----.-.-...-..-..-..--.-.-.."
    # dico = ["HELL", "HELLO", "OWORLD", "WORLD", "TEST"]
    dico = ['VGKEY', 'FJCXO', 'OGOCZ', 'IYXPP', 'QVTCA', 'CMFPY', 'VHPYX', 'GBDROR', 'JOJXX', 'QSEGW', 'QWEUN', 'MFMGR', 'YGNOH', 'OGHSE', 'BXVMH', 'ZZZMH', 'ORESONTTC', 'FRKZO', 'EZHAV', 'GSGZZ', 'RYDIP', 'QPRQZ', 'FFJGY', 'ECUBIH', 'UDHRD', 'UXUDG', 'YQVBS', 'KQNJD', 'ZSDIT', 'YWPZY', 'FDVPR', 'YXLTZY', 'MSNLV', 'TPTBY', 'NFJVW', 'BOVOY', 'ILGJN', 'ETWUG', 'ADOAY', 'BUCHG', 'GTHRO', 'KKPRT', 'ESTI', 'GXRFNA', 'IVSKM', 'TOXPM', 'UJHMZ', 'XDQTG', 'DLGZP', 'OJZAVU', 'MXDSX', 'JGINW', 'BZXGT', 'BXDMQ', 'DAXKGS', 'LVEIO', 'FNEOZ', 'ACQGD', 'GQZLV', 'DMXFA', 'FLUXK', 'XYQSAJ', 'DXDIB', 'IHCWB', 'WVYOF', 'BHLMH', 'CTUEL', 'RJOKE', 'VUJIN', 'UNSMY', 'KYINP', 'YIOJV', 'UNLVA', 'CCSRT', 'YNBUR', 'VDVAX', 'WSNCL', 'FWEKG', 'RVCHP', 'UYFGO', 'QGWJX', 'UKBKO', 'UUOCX', 'FLPNWA', 'ZRRUIN', 'ABXBS', 'QYJCB', 'BXDGD', 'QQOPA', 'XEMXM', 'IVCXP', 'SDXOJ', 'CHRKA', 'EHFFB', 'NWCIS', 'DAMDW', 'GPYXG', 'DKVZS', 'SSJEI', 'BZNBR', 'NBUDR', 'VTMLP', 'YCLHV', 'FHTAE', 'CLZQAQ', 'KXXNV', 'OSVTP', 'XZPAM', 'LNQIHY', 'WEARA', 'XXNQY', 'CGUK', 'TFPVG', 'WQUNA', 'ZPJXO', 'UWYUB', 'HGQDL', 'REMORSEP', 'BTVAQ', 'TGFIQ', 'UENC', 'QNHPT', 'GZBWS', 'NXXCR', 'EJTJN', 'ATVTP', 'OISZU', 'STGMKK', 'FSBQC', 'NEEAK', 'JFSZL', 'ARZVZ', 'KPPRE', 'FEFCG', 'BUSIT', 'IVOQA', 'NWNNA', 'GIFIO', 'VDZNEP', 'AJLCY', 'HJFEU', 'UNOJN', 'BAXZM', 'AMRIY', 'MKAEX', 'JSVVWR', 'VFEAJ', 'QFVSE', 'UEKNB', 'SFBQB', 'PNEET', 'ODNZR', 'BCCOKO', 'OXAHB', 'JMYLN', 'MJUXJ', 'EOUDAPPELEN', 'CDAHG', 'IXWKO', 'VQOKR', 'VFOIF', 'RJTXC', 'WAUVAH', 'LEOIK', 'AAKWH', 'LXGSB', 'WRMITJ', 'CZPOAV', 'NEWKP', 'ISLTJ', 'NJGME', 'SVYZD', 'THLAP', 'DSLYRT', 'AAKUR', 'SGSBK', 'VRMGA', 'SJTBKA', 'NJOVT', 'TJMWXD', 'VENIE', 'RSFR', 'LLMQC', 'VGNBA', 'TWWWS', 'WPQABJ', 'JXPHS', 'YFRXR', 'BFSHH', 'ERNWU', 'LKVSO', 'JSEPP', 'WLWKM', 'XSCBBV', 'RJNNA', 'ROHYZ', 'JCAQA', 'ALORSENUT', 'QQHGD', 'DNPFY', 'TQCVA', 'SLTQH', 'INTDB', 'LSKHJN', 'ZUOJKQ', 'KQDOLF', 'GPIQB', 'JROVT', 'MQNJML', 'UTFJK', 'VUBUQ', 'CQSLZ', 'UVISUELFL', 'OXQJO', 'JCIZS', 'KUSPV', 'BDDUT', 'VDSKU', 'POMLH', 'MVPUK', 'CKGTG', 'FMMCY', 'ZVRXZ', 'JOSFTZ', 'GYKCKU', 'YXINT', 'CXRHC', 'CPMUE', 'CHIFFRES', 'JVQBC', 'NRCEL', 'MKQDX', 'ZZVZIS', 'LBLRTQ', 'UJDBZ', 'BXTFY', 'NLHPM', 'VWTNM', 'EFYWP', 'DIUTU', 'PDPDOR', 'TVIAUNSIGNALR', 'XOTDP', 'TYNTT', 'OPTIMISERLEC', 'GETNBI', 'AXPMC', 'WGYLG', 'GKSVGL', 'MYFYB', 'CSRUK', 'GNQHM', 'CNVIO', 'BHPRTP', 'VBCYG', 'FDFEFJ', 'PDTEV', 'CIXRH', 'URDESFRQUENC', 'BYUQP', 'GPEPK', 'TKOQC', 'AEGAI', 'GFDVTW', 'TOAQF', 'CQWEQ', 'MENCEDCLINERLENT', 'ADVHT', 'IAKQZ', 'WPRHJ', 'VODLOF', 'UURSL', 'HSAHM', 'SOVPD', 'IDEPC', 'TAXZTB', 'KXFLY', 'HPVRB', 'TRJCE', 'ADVKM', 'JPYSC', 'JMBIW', 'EZPWVF', 'RPRFR', 'WSWHG', 'EZARN', 'IOYJY', 'AZBOX', 'HNKKX', 'KIRAY', 'DSVDG', 'CDYRCM', 'ELSCG', 'MUYIP', 'INTHH', 'ZIQLW', 'BIOTG', 'VSHLH', 'UWMUPM', 'SMYXCQ', 'LNPFAA', 'ZGJWA', 'UZNMH', 'CWZMM', 'HEOQK', 'YIXWR', 'OTCJR', 'RHPQIJ', 'ZAEIC', 'SOVNI', 'YWZNRG', 'MENBP', 'VXNMR', 'YYNUI', 'XBYLR', 'UKIJN', 'KXFJT', 'LFXCV', 'HRASESC', 'OXGFXW', 'VZYIYL', 'GEBSY', 'EMORSEESTCO', 'UTFHO', 'VLSOC', 'UEKWS', 'YWVIC', 'MAYXO', 'JLAMA', 'KQVPV', 'CWNDQ', 'VERSUNCB', 'EXTELAIDE', 'HXKCL', 'MSMPC', 'YRZFG', 'KMAJF', 'JYMSI', 'UAFJD', 'OOIWD', 'IBOJVV', 'WHTZI', 'KUTWID', 'GBVEG', 'CJAUG', 'BBUBN', 'PNQXE', 'ZDLWZR', 'IHNNR', 'FKUIQ', 'ETQGI', 'RNZAT', 'AKVQL', 'CZOSY', 'TGABV', 'KYZJR', 'CWZIA', 'PZUDL', 'KIZHN', 'VUBMC', 'EZANX', 'NEWNX', 'CZSBW', 'AQHZZV', 'XVSDR', 'SIIMK', 'QTXZS', 'VRGWI', 'JDBOUQ', 'CRXWU', 'SUGWE', 'AJMUU', 'DEONTE', 'BPEHQ', 'KNYIC', 'NTERMITTENT', 'XSOWK', 'OISLK', 'RSLFG', 'PUZSG', 'OFPPC', 'UKIQY', 'YOOZX', 'HLJLQ', 'WHBWB', 'DIAMQ', 'CZCJO', 'WDBWBD', 'JPYVE', 'JKJRRZ', 'XDCZY', 'GJOAG', 'OYVLZ', 'AOKODF', 'BOXTU', 'AUFJM', 'XIUME', 'AFBOE', 'QTFSL', 'LZCGA', 'YXITB', 'IHNSJ', 'ZHLPH', 'JTXDT', 'PZPGH', 'ACVYS', 'AYQPR', 'YLNRB', 'AINESETLE', 'UWKPA', 'TOQCK', 'OUUNGESTEC', 'ZDIHY', 'SMLTQ', 'OYFPW', 'UYMVO', 'BUIVR', 'LSGLT', 'AMRDZ', 'JPEZI', 'BVFOI', 'REYXPI', 'DDOEK', 'XTKYM', 'ZIQTA', 'UDBBW', 'VSEVMP', 'WFAKU', 'VKDAX', 'LYHPI', 'WVFDS', 'TTXJL']
    l_word = [word_to_morse(word) for word in dico]
    print("{}\n{}".format(dico, l_word))
    cpt = count(l, l_word, 0)
    print(cpt)
    print("total recu = {}".format(count.call))
