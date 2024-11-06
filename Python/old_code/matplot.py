import matplotlib.pyplot as plt
squres=[1,4,9,16,25]
fig,ax=plt.subplots()
ax.plot(squres,linewidth=3) #linewidth参数决定了绘制线条的粗细
ax.set_title("Square Numbers",fontsize=24)
ax.set_ylabel("Value",fontsize=14)
ax.set_xlabel("Square of Value",fontsize=14)
ax.tick_params(labelsize=24)
plt.show()  #打开Matplotlib查看器并显示绘图