package src;
import java.io.IOException;
import com.alien.enterpriseRFID.reader.AlienClass1Reader;
import com.alien.enterpriseRFID.reader.AlienReaderException;
import com.alien.enterpriseRFID.tags.Tag;

public class LeitorRfidCheckIn {
	private AlienClass1Reader reader = new AlienClass1Reader();

	public LeitorRfidCheckIn() throws Exception {
		reader.setConnection("192.168.8.54", 23);
		reader.setUsername("alien");
		reader.setPassword("password");
	}
	
	public void read() throws Exception {
		reader.open();
		Tag[] tagList = reader.getTagList();
		if (tagList == null || tagList.length >= 2) {
			System.out.println("Error");
		} else {
			System.out.println("TAG: " + tagList[0].getTagID());
		}
		reader.close();

	}
	
	public void encerrar() throws IOException{
		reader.close();
	}
	
	public static final void main(String args[]) throws Exception {
		
		LeitorRfidCheckIn leitor = new LeitorRfidCheckIn();
		try{
			leitor.read();
		} catch(AlienReaderException e){
			leitor.encerrar();
		}
	}
	
} 