module Exp07(input clk,input reset,input d,output reg q1,output reg q2);
always @(posedge clk or posedge reset)
if(reset) q1<=0;
else q1<=d;

always @(posedge clk or posedge reset)
if(reset) q2<=0;
else q2<=q1;
endmodule