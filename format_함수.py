format_a = "{}만 원".format(5000);
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000);
format_c = "{} {} {}".format(3000, 4000, 5000);
format_d = "{} {} {}".format(1, "문자열", True);

print(format_a); # 5000만 원
print(format_b); # 파이썬 열공하여 첫 연봉 5000만 원 만들기
print(format_c); # 3000 4000 5000
print(format_d); # 1 문자열 True

output_a = "{:d}".format(52);
output_b = "{:5d}".format(52);
output_c = "{:10d}".format(52);
output_d = "{:05d}".format(52);
output_e = "{:05d}".format(-52);

print(output_a); # 52
print(output_b); #    52
print(output_c); #         52
print(output_d); # 00052
print(output_e); # -0052

output_f = "{:+d}".format(52);
output_g = "{:+d}".format(-52);
output_h = "{: d}".format(52);
output_i = "{: d}".format(-52);

print(output_f); # +52
print(output_g); # -52
print(output_h); #  52
print(output_i); # -52

output_h = "{:+5d}".format(52);
output_i = "{:+5d}".format(-52);
output_j = "{:=+5d}".format(52);
output_k = "{:=+5d}".format(-52);
output_l = "{:+05d}".format(52);
output_m = "{:+05d}".format(-52);

print(output_h); #   +52
print(output_i); #   -52
print(output_j); # +  52
print(output_k); # -  52
print(output_l); # +0052
print(output_m); # -0052

output_n = "{:f}".format(52.273);
output_o = "{:15f}".format(52.273);
output_p = "{:+15f}".format(52.273);
output_q = "{:+015f}".format(52.273);

print(output_n); # 52.273000
print(output_o); #       52.273000
print(output_p); #      +52.273000
print(output_q); # +0000052.273000

output_r = "{:15.3f}".format(52.273);
output_s = "{:15.2f}".format(52.273);
output_t = "{:15.1f}".format(52.273);

print(output_r); #          52.273
print(output_s); #           52.27
print(output_t); #            52.3

output_u = 52.0
output_v = "{:g}".format(output_u);
print(output_u); # 52.0
print(output_v); # 52