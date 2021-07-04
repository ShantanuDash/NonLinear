set term png
set output 'lorenz.png'
splot "pl.dat" u 1:2:3 with lines
