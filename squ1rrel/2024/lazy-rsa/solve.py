#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes

if __name__ == "__main__":
    c = 11420169733597912638453974310976296342840438772934899653944946284527921765463891354182152294616337665313108085636067061251485792996493148094827999964385583364992542843630846911864602981658349693548380259629884212903554470004231160866680745154066318419977485221228944716844036265911222656710479650139274719426252576406561307088938784324291655853920727176132853663822020880574204790442647169649094846806057218165102873847070323190392619997632103724159815363319643022552432448214770378596825200154298562513279104608157870845848578603703757405758227316242247843290673221718467366000253484278487854736033323783510299081405
    p = 136883787266364340043941875346794871076915042034415471498906549087728253259343034107810407965879553240797103876807324140752463772912574744029721362424045513479264912763274224483253555686223222977433620164528749150128078791978059487880374953312009335263406691102746179899587617728126307533778214066506682031517
    q = 173071049014527992115134608840044450224804187710129859708853805709176487316207010402251651554296674942983458628001825388092613984020357016543095854903752286499436288875811897772811421580394898931781960982007306544027009178109074133665714245347548210688178519450728052309689045110008994598784658702110905581693
    n = p * q
    e = 65537

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, n)
    pt = long_to_bytes(m).decode()

    print(pt)
