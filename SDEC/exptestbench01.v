module exptestbench01;
reg [7:0] A,B;
wire [15:0] P;
Exp01 dut(A,B,P);
initial begin
A=5; B=3; #10;
A=10; B=4; #10;
A=15; B=6; #10;
$finish;
end
endmodule