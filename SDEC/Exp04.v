module Exp04(input clk,input reset,input read,input write,input [7:0] data_in,input [3:0] addr,output reg [7:0] data_out);
reg [7:0] mem [15:0];
always @(posedge clk) begin
if(write) mem[addr]<=data_in;
if(read) data_out<=mem[addr];
end
endmodule