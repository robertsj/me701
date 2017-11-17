import matplotlib.pyplot as plt
names = 'out_eig  out_gf_beo  out_ifavx_beo  out_if_beo  out_tuned_vaino  out_vaino'
for name in names.split():
    f = open(name, 'r')
    s = f.read().split() 
    f.close()
    n = list(map(float, s[1::4]))
    v = list(map(float, s[3::4]))
    plt.semilogx(n, v, label=name)

plt.xlabel('n')
plt.ylabel('MFLOPS/s')
plt.legend()
plt.show()
