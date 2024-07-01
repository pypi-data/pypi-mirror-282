module IIR #(
    parameter DW = 24,
    parameter COEFW = 18,
    parameter COEFQ = 16,
    parameter ORDER = 2,
    localparam N = (ORDER+1)*2
) (
    input  logic clk,
    input  logic rst,
    input  logic signed [DW-1:0] s_axis_tdata,
    input  logic s_axis_tvalid,
    output logic s_axis_tready,

    output logic signed [DW-1:0] m_axis_tdata,
    output logic m_axis_tvalid,
    input  logic m_axis_tready,

    input  logic signed [COEFW-1:0] coefs [N-1:0]
);

Skid #(.DW(DW)) skid_i (
    .clk,
    .rst,
    .s_axis_tdata,
    .s_axis_tvalid,
    .s_axis_tready,
    .m_axis_tdata,
    .m_axis_tvalid,
    .m_axis_tready
);

endmodule

