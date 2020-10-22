for i in range(101):
    a = pow(i,3)
    for j in range(2,i):
        b = pow(j,3)
        for k in range(j,i):
            c = pow(k,3)
            for n in range(k,i):
                d = pow(n,3)
                if a == (b+c+d):
                    print('Cube = {0}, Triple = ({1},{2},{3})'.format(i,j,k,n))
