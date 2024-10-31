interface Art{
    void enjoy();
    void create();
}

public class hello {
    public static void main(String[] args)
    {
        System.out.println("hello world");
        Music music= new Music();
        music.musiclong=100;
        music.musicname="\033[01;31m蔓越湖\033[0m";
        music.play(); 
        System.out.println("\n");
        music.create();
        music.enjoy();
    }
    
}

class Music implements Art{
    int musiclong;
    String musicname;
    
    @Override
    public void enjoy() {
        System.out.println("enjoy music");
        play();
    }

    @Override
    public void create() {
        musicname="the lake";
        musiclong=0;
        System.out.println("start enjoy\n");
        enjoy();
    }
    public void play(){
        String tip = String.format("Music %s,is play,it time is %d",musicname,musiclong, null);
        System.out.println(tip);
    }
}