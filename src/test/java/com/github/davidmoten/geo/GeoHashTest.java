package com.github.davidmoten.geo;

import com.google.common.collect.Sets;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.*;

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

//        try{
//
//        }catch (IllegalArgumentException e){
//            System.out.println(e);
//        }

        //e//
        assertEquals("114",GeoHash.adjacentHash("111",Direction.LEFT.opposite()));

        try {
            assertEquals("110", GeoHash.adjacentHash("", Direction.LEFT));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }

        assertEquals("110",GeoHash.adjacentHash("111",Direction.LEFT));
        assertEquals("0c",GeoHash.adjacentHash("11",Direction.LEFT));
        try{
            assertEquals("3",GeoHash.adjacentHash("ooo",Direction.LEFT));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }
        try{
            assertEquals("3",GeoHash.adjacentHash("oooo",Direction.LEFT));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }

        assertEquals("113",GeoHash.adjacentHash("111",Direction.TOP));
        assertEquals("14",GeoHash.adjacentHash("11",Direction.TOP));
        assertEquals("gzz",GeoHash.adjacentHash("ooo",Direction.TOP));
        try{
            assertEquals("3",GeoHash.adjacentHash("oooo",Direction.TOP));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }

    }

    @Test
    public void right() {
        //e//
        assertEquals("m",GeoHash.right("k"));
        assertEquals("ks",GeoHash.right("kk"));
        assertEquals("b",GeoHash.right("a"));
        assertEquals("bp",GeoHash.right("aa"));
    }

    @Test
    public void left() {
        //e//
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
        //e//
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
        //e//
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

    @Test
    public void adjacentHash1() {
        //e//
        assertEquals("113",GeoHash.adjacentHash("111",Direction.TOP,1));
        assertEquals("10c",GeoHash.adjacentHash("111",Direction.TOP,-1));
        assertEquals("14",GeoHash.adjacentHash("11",Direction.TOP,1));
        assertEquals("10",GeoHash.adjacentHash("11",Direction.TOP,-1));
        assertEquals("gzz",GeoHash.adjacentHash("ooo",Direction.TOP,1));
        try{
            assertEquals("4",GeoHash.adjacentHash("ooo",Direction.TOP,-1));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }
        try{
            assertEquals("4",GeoHash.adjacentHash("oo",Direction.TOP,1));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }
        try{
            assertEquals("4",GeoHash.adjacentHash("oo",Direction.TOP,-1));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(e);
        }
    }

    @Test
    public void neighbours() {
        //e//
        List<String> list = new ArrayList<String>();
        list.add("0");
        list.add("4");
        list.add("3");
        list.add("j");
        list.add("2");
        list.add("h");
        list.add("6");
        list.add("n");
        assertEquals(list,GeoHash.neighbours("1"));
        try {
            assertEquals(list,GeoHash.neighbours("a"));
        }catch (StringIndexOutOfBoundsException e){
            System.out.println(list);
        }
    }

    @Test
    public void encodeHash() {
        //e//
        assertEquals("v00000000000",GeoHash.encodeHash(45,45));
        assertEquals("f8j248j248j2",GeoHash.encodeHash(45,300));
        try{
            assertEquals(null,GeoHash.encodeHash(300,45));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }
        try{
            assertEquals(null,GeoHash.encodeHash(300,300));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }
    }

    @Test
    public void encodeHash1() {
        //e//
        assertEquals("v0",GeoHash.encodeHash(45,45,2));
        try{
             assertEquals("",GeoHash.encodeHash(45,45,-2));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }
        assertEquals("f8",GeoHash.encodeHash(45,300,2));
        try{
            assertEquals(null,GeoHash.encodeHash(45,300,-2));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }
        try{
            assertEquals(null,GeoHash.encodeHash(300,45,2));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }
        try{
            assertEquals(null,GeoHash.encodeHash(300,45,-2));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }
        try{
            assertEquals(null,GeoHash.encodeHash(300,300,2));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }
        try{
            assertEquals(null,GeoHash.encodeHash(300,300,-2));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }
    }

    @Test
    public void encodeHash2() {
        //e//
        LatLong testAdd = new LatLong(0,0);
        testAdd.add(45,45);
        assertEquals("s00000000000",GeoHash.encodeHash(testAdd));

        LatLong tt = new LatLong(45,45);
        assertEquals("v00000000000",GeoHash.encodeHash(tt));

        LatLong tf = new LatLong(45,300);
        assertEquals("f8j248j248j2",GeoHash.encodeHash(tf));

        try{
            LatLong ft = new LatLong(300,45);
            assertEquals("s00000000000",GeoHash.encodeHash(ft));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }

        try{
            LatLong ff = new LatLong(300,300);
            assertEquals("s00000000000",GeoHash.encodeHash(ff));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }

    }

    @Test
    public void encodeHash3() {
        //e//
        LatLong ttt = new LatLong(45,45);
        assertEquals("v0",GeoHash.encodeHash(ttt,2));

        try{
            LatLong ttf = new LatLong(45,45);
            assertEquals("v00000000000",GeoHash.encodeHash(ttf,-2));

        }catch (IllegalArgumentException e){
            System.out.println(e);
        }

        LatLong tft = new LatLong(45,300);
        assertEquals("f8",GeoHash.encodeHash(tft,2));

        try{
            LatLong tff = new LatLong(45,300);
            assertEquals("v00000000000",GeoHash.encodeHash(tff,-2));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }

        try{
            LatLong ftt = new LatLong(300,45);
            assertEquals("v00000000000",GeoHash.encodeHash(ftt,2));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }

        try{
            LatLong ftf = new LatLong(300,45);
            assertEquals("v00000000000",GeoHash.encodeHash(ftf,-2));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }

        try{
            LatLong fft = new LatLong(300,300);
            assertEquals("v00000000000",GeoHash.encodeHash(fft,2));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }

        try{
            LatLong fff = new LatLong(300,300);
            assertEquals("v00000000000",GeoHash.encodeHash(fff,-2));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }

    }

    @Test
    public void fromLongToString() {
        long hash =1;
        assertEquals("0",GeoHash.fromLongToString(hash));
        try {
            hash = 13;
            assertEquals("0",GeoHash.fromLongToString(hash));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }
        try {
            hash = 0;
            assertEquals("0",GeoHash.fromLongToString(hash));
        }catch (IllegalArgumentException e){
            System.out.println(e);
        }
    }

    @Test
    public void encodeHashToLong() {
        //e//
        assertEquals(0,GeoHash.encodeHashToLong(45,45,0));
        assertEquals(-2,GeoHash.encodeHashToLong(45,45,-2));
        assertEquals(0,GeoHash.encodeHashToLong(45,300,0));
        assertEquals(-2,GeoHash.encodeHashToLong(45,300,-2));
        assertEquals(0,GeoHash.encodeHashToLong(300,45,0));
        assertEquals(-2,GeoHash.encodeHashToLong(300,45,-2));
        assertEquals(0,GeoHash.encodeHashToLong(300,300,0));
        assertEquals(-2,GeoHash.encodeHashToLong(300,300,-2));

    }

    @Test
    public void decodeHash() {
        //e//
        String hashTest = "1";
        LatLong test = GeoHash.decodeHash(hashTest);
        assertEquals("LatLong [lat=-67.5, lon=-112.5]",test.toString());

        String hashTesta = "1a";
        LatLong testa = GeoHash.decodeHash(hashTesta);
        assertEquals("LatLong [lat=-47.8125, lon=-95.625]",testa.toString());

    }

    @Test
    public void hashLengthToCoverBoundingBox() {
        //e//
        assertEquals(12, GeoHash.hashLengthToCoverBoundingBox(10, 10, 10, 10));
        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(10, 10, 10, -10));
        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(10, 10, -10, 10));
        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(10, 10, -10, -10));

        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(10, -10, 10, 10));
        assertEquals(12, GeoHash.hashLengthToCoverBoundingBox(10, -10, 10, -10));
        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(10, -10, -10, 10));
        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(10, -10, -10, -10));

        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(-10, 10, 10, 10));
        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(-10, 10, 10, -10));
        assertEquals(12, GeoHash.hashLengthToCoverBoundingBox(-10, 10, -10, 10));
        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(-10, 10, -10, -10));

        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(-10, -10, 10, 10));
        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(-10, -10, 10, -10));
        assertEquals(0, GeoHash.hashLengthToCoverBoundingBox(-10, -10, -10, 10));
        assertEquals(12, GeoHash.hashLengthToCoverBoundingBox(-10, -10, -10, -10));
    }

    @Test
    public void hashContains() {
        LatLong centre = GeoHash.decodeHash("0");
        assertTrue(GeoHash.hashContains("0", centre.getLat(), centre.getLon()));
        assertTrue(GeoHash.hashContains("0", centre.getLat() + 20, centre.getLon()));
        assertFalse(GeoHash.hashContains("0", centre.getLat(),centre.getLon() + 50));
    }

    @Test
    public void coverBoundingBox() {
//        Set<String>test = GeoHash.coverBoundingBox(0,0,0,0).getHashes();
//        assertEquals(Sets.newHashSet("s00000000000"),GeoHash.coverBoundingBox(0,0,0,0).getHashes());

        assertEquals(Sets.newHashSet("s1z0gs3y0zh7"),GeoHash.coverBoundingBox(10,10,10,10).getHashes());
    }

    @Test(expected = IllegalArgumentException.class)
    public void coverBoundingBoxMaxHashes() {
        //e//
        Coverage coverageMax = GeoHash.coverBoundingBoxMaxHashes(0,0,0,0,12);
        assertEquals(1,coverageMax.getHashes().size());


        Coverage coverageMin = GeoHash.coverBoundingBoxMaxHashes(0,0,0,0,0);
        try{
            assertEquals(1,coverageMin.getHashes().size());
        }catch (NullPointerException e){
            System.out.println(e);
        }

        Coverage coverageOne = GeoHash.coverBoundingBoxMaxHashes(0,0,0,0,1);
        assertEquals(1,coverageOne.getHashes().size());

        Coverage coverageMoreMax = GeoHash.coverBoundingBoxMaxHashes(0,0,0,0,Integer.MAX_VALUE);
        try{
            assertEquals(1,coverageMoreMax.getHashes().size());
        }catch (NullPointerException e){
            System.out.println(e);
        }

        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,10,10,10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,10,10,-10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,10,-10,10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,10,-10,-10,12).getHashes().size());

        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,-10,10,10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,-10,10,-10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,-10,-10,10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,-10,-10,-10,12).getHashes().size());

        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,10,10,10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,10,10,-10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,10,-10,10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,10,-10,-10,12).getHashes().size());

        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,-10,10,10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,-10,10,-10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,-10,-10,10,12).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,-10,-10,-10,12).getHashes().size());

        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,10,10,10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,10,10,-10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,10,-10,10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,10,-10,-10,0).getHashes().size());

        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,-10,10,10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,-10,10,-10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,-10,-10,10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(10,-10,-10,-10,0).getHashes().size());

        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,10,10,10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,10,10,-10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,10,-10,10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,10,-10,-10,0).getHashes().size());

        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,-10,10,10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,-10,10,-10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,-10,-10,10,0).getHashes().size());
        assertEquals(1,GeoHash.coverBoundingBoxMaxHashes(-10,-10,-10,-10,0).getHashes().size());
    }

    @Test
    public void coverBoundingBox1() {
        assertEquals(1,GeoHash.coverBoundingBox(0,0,0,0,1).getHashLength());
    }

//    @Test
//    public void coverBoundingBoxLongs() {
//    }

    @Test
    public void heightDegrees() {
        //e//
        assertEquals(4.190951585769653E-8,GeoHash.heightDegrees(15),0.0000001);
        assertEquals(0.0439453125,GeoHash.heightDegrees(5),0.0000001);
        try {
            assertEquals(123, GeoHash.heightDegrees(-5), 0.0000001);
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println(e);
        }
    }

    @Test
    public void widthDegrees() {
        //e//
        assertEquals(1.3096723705530167E-9,GeoHash.widthDegrees(15),0.0000001);
        assertEquals(0.0439453125,GeoHash.widthDegrees(5),0.0000001);
        try {
            assertEquals(123,GeoHash.widthDegrees(-5),0.0000001);
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println(e);
        }
    }

    @Test
    public void gridAsString() {
        Set<String>test = new TreeSet<String>();
        test.add("f");
        assertEquals("c F g \n" + "9 d e \n" + "3 6 7 \n",GeoHash.gridAsString("d", 1,test));
    }

    @Test
    public void gridAsString1() {
        assertEquals("c f g \n" + "9 d e \n" + "3 6 7 \n",GeoHash.gridAsString("d", -1, -1, 1, 1));
    }

    @Test
    public void gridAsString2() {
        Set<String>test = new TreeSet<String>();
        test.add("f");
        assertEquals("c F g \n" +
                "9 d e \n" +
                "3 6 7 \n",GeoHash.gridAsString("d",-1,-1,1,1,test));
    }
}