module Exp03 #(parameter DATA_WIDTH=8)(input clk,input reset,input start,input [DATA_WIDTH-1:0] data_in,output reg tx);
reg [1:0] state;
parameter IDLE=0,START=1,DATA=2,STOP=3;

always @(posedge clk or posedge reset)
if(reset) state<=IDLE;
else case(state)
IDLE: if(start) state<=START;
START: state<=DATA;
DATA: state<=STOP;
STOP: state<=IDLE;
endcase

always @(*) begin
case(state)
IDLE: tx=1;
START: tx=0;
DATA: tx=data_in[0];
STOP: tx=1;
endcase
end
endmodule