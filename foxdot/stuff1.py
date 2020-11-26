p1 >> dirt(var([1,2,3,-2],2), dur=[0.5])

p2 >> dirt(Pvar([1,-2,1,2],4).arp([0,1,2]),oct=6,dur=P[1/2,3/2,1]/2)


q1 >> quin([0,-1,0,-2],dur=8,drive=0.2,vib=0.5,oct=4,chop=32)
q2 >> quin(q1.pitch,chop=16,dur=8)

p3 >> zap([0],dur=[8],drive=0.5,sus=p3.dur,vib=0,vibdepth=0,dist=0.3,glide=-1,cut=0,glidedelay=0.5,room=0,mix=0,formant=0,decay=0.1,chop=[8,16,32,16])

d1 >> play("X ")


p2 >> play("-(-=)",dur=[0.5])

print(SynthDefs)
