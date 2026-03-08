module Exp06(input clk,input a,input b,output reg y);
reg temp;
always @(posedge clk) temp<=a&b;
always @(posedge clk) y<=temp;
endmodule