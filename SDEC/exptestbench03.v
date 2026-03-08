module exptestbench03;
reg clk,reset,start;
reg [7:0] data_in;
wire tx;
Exp03 dut(clk,reset,start,data_in,tx);
always #5 clk=~clk;
initial begin
clk=0; reset=1; start=0; data_in=8'hAA;
#10 reset=0;
#10 start=1;
#10 start=0;
#100 $finish;
end
endmodule