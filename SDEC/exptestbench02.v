module exptestbench02;
reg clk,reset;
wire [3:0] green;
Exp02 dut(clk,reset,green);
always #5 clk=~clk;
initial begin
clk=0; reset=1;
#10 reset=0;
#100 $finish;
end
endmodule