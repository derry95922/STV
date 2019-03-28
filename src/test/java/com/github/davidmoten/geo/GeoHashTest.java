package com.github.davidmoten.geo;

import com.google.common.collect.Sets;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import static com.github.davidmoten.geo.GeoHash.decodeHash;
import static org.junit.Assert.*;

public class GeoHashTest {
    String hash;
    Direction direction;
    @Before
    public void setUp() throws Exception {
        hash = "1";
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void adjacentHash() {
        //*//
        assertEquals("3",GeoHash.adjacentHash(hash,Direction.TOP));
        String test = "";
        try{
            assertEquals("3",GeoHash.adjacentHash(test,Direction.TOP));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }
        test = "11";
        assertEquals("14",GeoHash.adjacentHash(test,Direction.TOP));
        test = test + "1";
        assertEquals("113",GeoHash.adjacentHash(test,Direction.TOP));


//        assertEquals("113",GeoHash.adjacentHash("",Direction.TOP));
    }

    @Test
    public void right() {
        //*//
//        assertEquals("4",GeoHash.right(hash));
        assertEquals("m",GeoHash.right("k"));
        assertEquals("ks",GeoHash.right("kk"));
        assertEquals("b",GeoHash.right("a"));
        assertEquals("bp",GeoHash.right("aa"));

    }

    @Test
    public void left() {
        //*//
//        assertEquals("0",GeoHash.left(hash));
        assertEquals("7",GeoHash.left("k"));
        assertEquals("kh",GeoHash.left("kk"));
        try {
            assertEquals("b", GeoHash.left("a"));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }
        try {
            assertEquals("b", GeoHash.left("aa"));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }
    }

    @Test
    public void top() {
        //*//
//        assertEquals("3",GeoHash.top(hash));
        assertEquals("s",GeoHash.top("k"));
        assertEquals("km",GeoHash.top("kk"));
        assertEquals("g", GeoHash.top("a"));
        try {
            assertEquals("b", GeoHash.top("aa"));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }
    }

    @Test
    public void bottom() {
        //*//
//        assertEquals("j",GeoHash.bottom(hash));
        assertEquals("h",GeoHash.bottom("k"));
        assertEquals("k7",GeoHash.bottom("kk"));
        try {
            assertEquals("b", GeoHash.bottom("a"));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }
        try {
            assertEquals("b", GeoHash.bottom("aa"));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }
    }
//*new here*//
    @Test
    public void adjacentHash1() {
        //*//
        String test = "test5278";
        assertEquals("1",GeoHash.adjacentHash(hash,Direction.BOTTOM,0));
        assertEquals("3",GeoHash.adjacentHash(hash,Direction.BOTTOM,-1));
        assertEquals("j",GeoHash.adjacentHash(hash,Direction.TOP,-1));
        assertEquals("0",GeoHash.adjacentHash(hash,Direction.RIGHT,-1));
        assertEquals("4",GeoHash.adjacentHash(hash,Direction.LEFT,-1));
    }

    @Test
    public void neighbours() {
        //*//
        List<String> list = new ArrayList<String>();
        String left = GeoHash.adjacentHash(hash, Direction.LEFT);
        String right = GeoHash.adjacentHash(hash, Direction.RIGHT);
        list.add(left);
        list.add(right);
        list.add(GeoHash.adjacentHash(hash, Direction.TOP));
        list.add(GeoHash.adjacentHash(hash, Direction.BOTTOM));
        list.add(GeoHash.adjacentHash(left, Direction.TOP));
        list.add(GeoHash.adjacentHash(left, Direction.BOTTOM));
        list.add(GeoHash.adjacentHash(right, Direction.TOP));
        list.add(GeoHash.adjacentHash(right, Direction.BOTTOM));
        assertEquals(list,GeoHash.neighbours(hash));
    }

    @Test
    public void encodeHash() {
        //*//
        assertEquals("s00000000000",GeoHash.encodeHash(0,0));
    }

    @Test
    public void encodeHash1() {
        //*//
        assertEquals("s0",GeoHash.encodeHash(0,0,2));

        try{
            assertEquals("s0",GeoHash.encodeHash(0,0,112));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }

        try{
            assertEquals("s0",GeoHash.encodeHash(91,0,2));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }

        try{
            assertEquals("s0",GeoHash.encodeHash(-91,0,2));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }
    }

    @Test
    public void encodeHash2() {
        LatLong p = new LatLong(0,0);
        assertEquals("s00000000000",GeoHash.encodeHash(p));
    }

    @Test
    public void encodeHash3() {
        LatLong p = new LatLong(0,0);
        assertEquals("s00000000000",GeoHash.encodeHash(p,12));

    }

    @Test
    public void fromLongToString() {
        //*//
        long hash =1;
        assertEquals("0",GeoHash.fromLongToString(hash));
        try {
            hash = 0;
            assertEquals("0",GeoHash.fromLongToString(hash));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }
        try {
            hash = 13;
            assertEquals("0",GeoHash.fromLongToString(hash));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }
    }

    @Test
    public void encodeHashToLong() {
        assertEquals(0, GeoHash.encodeHashToLong(0, 0, 0));
    }

//    @Test
//    public void decodeHash() {
//        //*//
//        String geoHash = "0";
//        String BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz";
//        int[] BITS = new int[] { 16, 8, 4, 2, 1 };
//
//        boolean isEven = true;
//        double[] lat = new double[2];
//        double[] lon = new double[2];
//        lat[0] = -90.0;
//        lat[1] = 90.0;
//        lon[0] = -180.0;
//        lon[1] = 180.0;
//
//        for (int i = 0; i <geoHash.length(); i++) {
//            char c = geoHash.charAt(i);
//            int cd = BASE32.indexOf(c);
//            for (int j = 0; j < 5; j++) {
//                int mask = BITS[j];
//                if (isEven) {
//                    if ((cd & mask) != 0)
//                        lon[0] = (lon[0] + lon[1]) / 2;
//                    else
//                        lon[1] = (lon[0] + lon[1]) / 2;
//                } else {
//                    if ((cd & mask) != 0)
//                        lat[0] = (lat[0] + lat[1]) / 2;
//                    else
//                        lat[1] = (lat[0] + lat[1]) / 2;
//                }
//                isEven = !isEven;
//            }
//        }
//        double resultLat = (lat[0] + lat[1]) / 2;
//        double resultLon = (lon[0] + lon[1]) / 2;
//
//        LatLong test = new LatLong(resultLat,resultLon);
//
//        assertEquals(test,GeoHash.decodeHash("0"));
//    }

    @Test
    public void hashLengthToCoverBoundingBox() {
        assertEquals(0,
                GeoHash.hashLengthToCoverBoundingBox(10, -10, -10, 10));
        assertEquals(12,
                GeoHash.hashLengthToCoverBoundingBox(10, -10, 10, -10));
        assertEquals(0,
                GeoHash.hashLengthToCoverBoundingBox(1, 10, 10, -10));
        assertEquals(0,
                GeoHash.hashLengthToCoverBoundingBox(-10, -10, 10, 10));
        assertEquals(1,
                GeoHash.hashLengthToCoverBoundingBox(7, 10, 15, 10));
    }

    @Test
    public void hashContains() {
        LatLong centre = decodeHash("0");
        assertTrue(GeoHash.hashContains("0", centre.getLat(), centre.getLon()));
        assertTrue(GeoHash.hashContains("0", centre.getLat() + 20, centre.getLon()));
        assertFalse(GeoHash.hashContains("0", centre.getLat(),centre.getLon() + 50));
    }

    @Test
    public void coverBoundingBox() {
        Set<String>test = GeoHash.coverBoundingBox(0,0,0,0).getHashes();
        assertEquals(Sets.newHashSet("s00000000000"),test);
//        assertEquals(1,GeoHash.coverBoundingBox(0,0,0,0,1).getHashLength());
    }

    @Test
    public void coverBoundingBoxMaxHashes() {
        Coverage coverageMax = GeoHash.coverBoundingBoxMaxHashes(0,0,0,0,12);
        assertEquals(1,coverageMax.getHashes().size());

        Coverage coverageMin = GeoHash.coverBoundingBoxMaxHashes(0,0,0,0,0);
        assertNull(coverageMin);

        Coverage coverageOne = GeoHash.coverBoundingBoxMaxHashes(0,0,0,0,1);
        assertEquals(1,coverageOne.getHashes().size());

        Coverage coverageMoreMax = GeoHash.coverBoundingBoxMaxHashes(0,0,0,0,Integer.MAX_VALUE);
        assertEquals(GeoHash.MAX_HASH_LENGTH,coverageMoreMax.getHashLength());
    }

    @Test
    public void coverBoundingBox1() {
        assertEquals(1,GeoHash.coverBoundingBox(0,0,0,0,1).getHashLength());
    }

//    @Test
//    public void coverBoundingBoxLongs() {
//    }
//
    @Test
    public void heightDegrees() {
        //*//
        assertEquals(45.0,GeoHash.heightDegrees(1),0.0000001);
        assertEquals(4.190951585769653E-8,GeoHash.heightDegrees(13),0.0000001);
    }

    @Test
    public void widthDegrees() {
        //*//
        assertEquals(45.,GeoHash.widthDegrees(1),0.0000001);
        assertEquals(4.190951585769653E-8,GeoHash.widthDegrees(13),0.0000001);
    }

    @Test
    public void gridAsString() {
//        System.out.println(GeoHash.gridAsString(hash, -5, -5, 5, 5));
//        System.out.println(gridAsString("dr", 1,
//                Collections.<String> emptySet()));
//        assertEquals("",GeoHash.gridAsString(hash,0,0,0,0));
    }
//
//    @Test
//    public void gridAsString1() {
//    }
//
//    @Test
//    public void gridAsString2() {
//    }
}