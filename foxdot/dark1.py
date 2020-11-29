ritmo = P[4,0.5,1.5,4,2]


Scale.default='minorPentatonic'

p1.reset() >> dirt(var([[0,0,0,3],0,1,[-2,[3,-2]],-2],ritmo),dur=ritmo/1,drive=linvar([0.3,0.5],16),amp=var([1,[1,1]],[12,4]),oct=(5,6),vib=4,vibdepth=0.01,formant=(3,2,4)).solo() #P[0].arp([0,1,2])

p2 >> zap(var([0,1,2,-2,0,1],[10,2,2,2,2,2]),drive=0.3,oct=var([5,5,6],1/3),dur=[0.5],echo=0.3).stop()

q1 >> play("q",drive=0.05,dur=P(PSum(5,8),PDur(5,8)),pshift=var([0,3,0,0],4))

d1 >> play(":(-:-=)",sample=[2,1],dur=PRand([0.25,0.5])[:10])

d2 >> play("x( X)", pan=linvar([-1,1],16))

d3 >> play("  X ",sample=6)

o1 >> play("   ([o ] )",sample=3)


print(P+[0,1,2,3])





