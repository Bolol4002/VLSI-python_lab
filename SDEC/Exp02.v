module Exp02(input clk, input reset, output reg [3:0] green);
reg [1:0] state;
always @(posedge clk or posedge reset)
if(reset) state<=0;
else state<=state+1;

always @(*) begin
case(state)
0: green=4'b0001;
1: green=4'b0010;
2: green=4'b0100;
3: green=4'b1000;
endcase
end
endmodule