package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

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
        assertEquals("3",GeoHash.adjacentHash(hash,Direction.TOP));
    }

    @Test
    public void right() {
        assertEquals("4",GeoHash.adjacentHash(hash,Direction.RIGHT));
    }

    @Test
    public void left() {
        assertEquals("0",GeoHash.adjacentHash(hash,Direction.LEFT));
    }

    @Test
    public void top() {
        assertEquals("3",GeoHash.adjacentHash(hash,Direction.TOP));
    }

    @Test
    public void bottom() {
        assertEquals("j",GeoHash.adjacentHash(hash,Direction.BOTTOM));
    }

//    @Test
//    public void adjacentHash1() {
//    }
//
//    @Test
//    public void neighbours() {
//    }
//
//    @Test
//    public void encodeHash() {
//    }
//
//    @Test
//    public void encodeHash1() {
//    }
//
//    @Test
//    public void encodeHash2() {
//    }
//
//    @Test
//    public void encodeHash3() {
//    }
//
//    @Test
//    public void fromLongToString() {
//    }
//
//    @Test
//    public void encodeHashToLong() {
//    }
//
//    @Test
//    public void decodeHash() {
//    }
//
//    @Test
//    public void hashLengthToCoverBoundingBox() {
//    }
//
//    @Test
//    public void hashContains() {
//    }
//
//    @Test
//    public void coverBoundingBox() {
//    }
//
//    @Test
//    public void coverBoundingBoxMaxHashes() {
//    }
//
//    @Test
//    public void coverBoundingBox1() {
//    }
//
//    @Test
//    public void coverBoundingBoxLongs() {
//    }
//
//    @Test
//    public void heightDegrees() {
//    }
//
//    @Test
//    public void widthDegrees() {
//    }
//
//    @Test
//    public void gridAsString() {
//    }
//
//    @Test
//    public void gridAsString1() {
//    }
//
//    @Test
//    public void gridAsString2() {
//    }
}