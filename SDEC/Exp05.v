module Exp05(input clk,input reset,input d,output reg q);
always @(posedge clk or posedge reset)
if(reset) q<=0;
else q<=d;
endmodule