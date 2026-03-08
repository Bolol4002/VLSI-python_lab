module exptestbench08;
reg a,b;
wire y;
Exp08 dut(a,b,y);
initial begin
a=0;b=0;
#10 b=1;
#10 a=1;b=0;
#10 a=1;b=1;
#20 $finish;
end
endmodule