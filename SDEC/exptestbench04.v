module exptestbench04;
reg clk,reset,read,write;
reg [7:0] data_in;
reg [3:0] addr;
wire [7:0] data_out;
Exp04 dut(clk,reset,read,write,data_in,addr,data_out);
always #5 clk=~clk;
initial begin
clk=0; read=0; write=1; addr=2; data_in=8'hAA;
#10 write=0; read=1;
#20 $finish;
end
endmodule