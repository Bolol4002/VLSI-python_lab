module exptestbench06;
reg clk,a,b;
wire y;
Exp06 dut(clk,a,b,y);
always #5 clk=~clk;
initial begin
clk=0; a=0; b=0;
#10 a=1;
#10 b=1;
#20 $finish;
end
endmodule