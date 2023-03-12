#!/usr/bin/env python3

def mod_inverse(A, M):
    m0 = M
    y = 0
    x = 1

    if (M == 1):
        return 0

    while (A > 1):
        q = A // M

        t = M

        M = A % M
        A = t
        t = y

        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x


if __name__ == "__main__":
    f = 3954523654845598592730156937269688140867480061118457307435945875579028695730063528424973907208923014508950419982702682082417623843946231057553311028711409093751376287876799688357176816093484535703797332422565021382453879908968161161537921292725907853309522100738603080298951279637316809695591295752657105226749125868510570125512146397480808774515489938198191435285342823923715673372695893409325086032930406554421670815433958591841773705563688270739343539481283865883427560667086249616210745997056621098406247201301461721906304555526293017773805845093545204570993288514598261070097976786800172141678030841959348372097
    n = 21429933885346644587620272790089165813353259223649897308397918491861562279767580488441831451651834802520437234248670652477414296159324726172158330221397420877323921934377321483041598028053870169281419856238830264612049920637819183013812186448416408328958360799645342598727238977986741643705720539702955864527935398839069236768630867447760912744208154645904678859979378604386855741350220991958191408182147658532111413386776058224418484895056146180001830405844881486308594953615999140110712045286000170660686758188247928230655746746482354748673482506070246808187808961599576834080344066055446605664648340486804023919467
    e = 10788856448030235429585145974385410619185237539198378911887172763282204686697141640582780419040340318300048024100764883750608733331571719088729202796193207904701854848679412033514037149161609202467086017862616635522167577463675349103892366486246290794304652162107619408011548841664240624935414339021041162505899467159623692906986841033101688573177710503499081107294555688550493634416552587963816327790111808356639558596438537569271043190414208204773219496030644456745185896540608008662177117212000718802474957268532153146989410300300554162811564064457762004188326986236869603714437275058878379647196886872404148116134

    inverse = mod_inverse(e, n)
    x = inverse % n
    flag = (f * x) % n
    print(bytes.fromhex(hex(flag)[2:]).decode('utf-8'))
