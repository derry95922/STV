package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class Base32Test {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void encodeBase32() {
        assertEquals("79",Base32.encodeBase32(233,2));
        assertEquals("-001",Base32.encodeBase32(-1,3));
    }

    @Test
    public void encodeBase321() {
        assertEquals("000000000082",Base32.encodeBase32(258));
    }

    @Test
    public void decodeBase32() {
        assertEquals(1091,Base32.decodeBase32("123"));
        assertEquals(-1,Base32.decodeBase32("-1"));
    }

    @Test
    public void getCharIndex() {
        assertEquals(1,Base32.getCharIndex('1'));
        try{
            assertEquals("not a base32 character: " + '_',Base32.getCharIndex('_'));
        }catch (IllegalArgumentException e){
            System.out.print(e);
        }

    }

    @Test
    public void padLeftWithZerosToLength() {
        assertEquals("0123",Base32.padLeftWithZerosToLength("123",4));
    }
}