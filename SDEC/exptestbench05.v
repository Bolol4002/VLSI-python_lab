module exptestbench05;
reg clk,reset,d;
wire q;
Exp05 dut(clk,reset,d,q);
always #5 clk=~clk;
initial begin
clk=0; reset=1; d=0;
#10 reset=0;
#10 d=1;
#20 d=0;
#50 $finish;
end
endmodule