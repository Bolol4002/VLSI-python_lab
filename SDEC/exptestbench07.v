module exptestbench07;
reg clk,reset,d;
wire q1,q2;
Exp07 dut(clk,reset,d,q1,q2);
always #5 clk=~clk;
initial begin
clk=0; reset=1; d=0;
#10 reset=0;
#10 d=1;
#30 $finish;
end
endmodule